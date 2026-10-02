from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)

from config import SECRET_KEY, DEBUG
from database import (
    init_db,
    save_assessment,
    get_assessment,
    get_dashboard_stats
)

from services.questionnaire import get_questions
from services.feature_engine import extract_privacy_features
from services.scoring_engine import (
    calculate_category_scores,
    calculate_privacy_risk
)

from services.findings_engine import (
    generate_privacy_findings
)

from services.recommendation_engine import (
    generate_recommendations
)

from services.improvement_simulator import (
    simulate_improvement
)


app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024

init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assessment")
def assessment():
    return render_template(
        "assessment.html",
        questions=get_questions()
    )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/report/<assessment_id>")
def report(assessment_id):
    result = get_assessment(assessment_id)

    if not result:
        return "Assessment not found", 404

    return render_template(
        "report.html",
        result=result
    )


@app.get("/api/questions")
def api_questions():
    return jsonify({
        "questions": get_questions()
    })


@app.post("/api/assessment")
def create_assessment():

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "Request body must be a JSON object."
        }), 400

    questions = get_questions()

    required_fields = [
        question["id"]
        for question in questions
    ]

    missing = [
        field
        for field in required_fields
        if field not in payload
    ]

    if missing:
        return jsonify({
            "error": "Missing required fields.",
            "fields": missing
        }), 400

    features = extract_privacy_features(
        payload
    )

    category_scores = calculate_category_scores(
        features
    )

    risk = calculate_privacy_risk(
        category_scores
    )

    findings = generate_privacy_findings(
        payload,
        features,
        category_scores
    )

    recommendations = generate_recommendations(
        findings
    )

    assessment_id = str(uuid4())

    created_at = datetime.now(
        timezone.utc
    ).isoformat()

    save_assessment(
        assessment_id=assessment_id,
        overall_score=risk["overall_score"],
        risk_level=risk["risk_level"],
        category_scores=category_scores,
        findings=findings,
        recommendations=recommendations,
        created_at=created_at
    )

    return jsonify({
        "assessment_id": assessment_id,
        "overall_score": risk["overall_score"],
        "risk_level": risk["risk_level"],
        "category_scores": category_scores,
        "findings": findings,
        "recommendations": recommendations,
        "report_url": (
            f"/report/{assessment_id}"
        )
    }), 201


@app.get("/api/assessment/<assessment_id>")
def api_get_assessment(assessment_id):

    result = get_assessment(
        assessment_id
    )

    if not result:
        return jsonify({
            "error": "Assessment not found."
        }), 404

    return jsonify(result)


@app.get("/api/assessment/<assessment_id>/recommendations")
def api_recommendations(assessment_id):

    result = get_assessment(
        assessment_id
    )

    if not result:
        return jsonify({
            "error": "Assessment not found."
        }), 404

    return jsonify({
        "assessment_id": assessment_id,
        "recommendations": result[
            "recommendations"
        ]
    })


@app.post("/api/assessment/simulate-improvement")
def api_simulate_improvement():

    payload = request.get_json(
        silent=True
    )

    if not isinstance(payload, dict):
        return jsonify({
            "error": "JSON body required."
        }), 400

    data = payload.get("current_data")

    changes = payload.get("changes")

    if not isinstance(data, dict):
        return jsonify({
            "error": "current_data must be an object."
        }), 400

    if not isinstance(changes, dict):
        return jsonify({
            "error": "changes must be an object."
        }), 400

    result = simulate_improvement(
        data,
        changes
    )

    return jsonify(result)


@app.get("/api/dashboard/stats")
def api_dashboard_stats():

    return jsonify(
        get_dashboard_stats()
    )


@app.get("/api/privacy-checklist")
def privacy_checklist():

    checklist = [
        "Review profile visibility",
        "Hide unnecessary contact information",
        "Review birth-date visibility",
        "Review location sharing",
        "Avoid unnecessary real-time location posts",
        "Review tagging permissions",
        "Review followers/friends",
        "Verify unfamiliar requests",
        "Enable MFA",
        "Enable login alerts",
        "Review active sessions",
        "Review connected apps",
        "Remove unused integrations",
        "Review old public posts",
        "Review photo privacy",
        "Be cautious with unexpected links",
        "Never share verification codes",
        "Review privacy settings periodically"
    ]

    return jsonify({
        "checklist": checklist
    })


@app.errorhandler(413)
def request_too_large(error):

    return jsonify({
        "error": "Request payload is too large."
    }), 413


@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "error": "Internal server error."
    }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=DEBUG
    )