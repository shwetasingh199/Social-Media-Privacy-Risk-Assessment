import sqlite3
from config import DATABASE_PATH


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            assessment_id TEXT PRIMARY KEY,
            overall_score REAL NOT NULL,
            risk_level TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS category_scores (
            category_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id TEXT NOT NULL,
            category TEXT NOT NULL,
            score REAL NOT NULL,
            FOREIGN KEY (assessment_id)
                REFERENCES assessments(assessment_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS findings (
            finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id TEXT NOT NULL,
            category TEXT NOT NULL,
            finding_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (assessment_id)
                REFERENCES assessments(assessment_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id TEXT NOT NULL,
            finding_type TEXT NOT NULL,
            recommendation TEXT NOT NULL,
            priority TEXT NOT NULL,
            FOREIGN KEY (assessment_id)
                REFERENCES assessments(assessment_id)
        )
    """)

    connection.commit()
    connection.close()


def save_assessment(
    assessment_id,
    overall_score,
    risk_level,
    category_scores,
    findings,
    recommendations,
    created_at
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO assessments
        (assessment_id, overall_score, risk_level, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            assessment_id,
            overall_score,
            risk_level,
            created_at
        )
    )

    for category, score in category_scores.items():
        cursor.execute(
            """
            INSERT INTO category_scores
            (assessment_id, category, score)
            VALUES (?, ?, ?)
            """,
            (
                assessment_id,
                category,
                score
            )
        )

    for finding in findings:
        cursor.execute(
            """
            INSERT INTO findings
            (
                assessment_id,
                category,
                finding_type,
                severity,
                description
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                assessment_id,
                finding["category"],
                finding["finding_type"],
                finding["severity"],
                finding["description"]
            )
        )

    for recommendation in recommendations:
        cursor.execute(
            """
            INSERT INTO recommendations
            (
                assessment_id,
                finding_type,
                recommendation,
                priority
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                assessment_id,
                recommendation["finding_type"],
                recommendation["recommendation"],
                recommendation["priority"]
            )
        )

    connection.commit()
    connection.close()


def get_assessment(assessment_id):
    connection = get_connection()

    assessment = connection.execute(
        """
        SELECT *
        FROM assessments
        WHERE assessment_id = ?
        """,
        (assessment_id,)
    ).fetchone()

    categories = connection.execute(
        """
        SELECT category, score
        FROM category_scores
        WHERE assessment_id = ?
        """,
        (assessment_id,)
    ).fetchall()

    findings = connection.execute(
        """
        SELECT category, finding_type, severity, description
        FROM findings
        WHERE assessment_id = ?
        """,
        (assessment_id,)
    ).fetchall()

    recommendations = connection.execute(
        """
        SELECT finding_type, recommendation, priority
        FROM recommendations
        WHERE assessment_id = ?
        """,
        (assessment_id,)
    ).fetchall()

    connection.close()

    if not assessment:
        return None

    return {
        "assessment": dict(assessment),
        "category_scores": [dict(x) for x in categories],
        "findings": [dict(x) for x in findings],
        "recommendations": [dict(x) for x in recommendations]
    }


def get_dashboard_stats():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) AS count FROM assessments"
    ).fetchone()["count"]

    distribution = connection.execute(
        """
        SELECT risk_level, COUNT(*) AS count
        FROM assessments
        GROUP BY risk_level
        """
    ).fetchall()

    average = connection.execute(
        """
        SELECT AVG(overall_score) AS average
        FROM assessments
        """
    ).fetchone()["average"]

    connection.close()

    return {
        "total_assessments": total,
        "average_score": round(average or 0, 2),
        "risk_distribution": [dict(x) for x in distribution]
    }