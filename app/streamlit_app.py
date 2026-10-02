import os
import sys

import streamlit as st


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from services.predictor import PrivacyRiskPredictor


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Social Media Privacy Risk Assessment",
    page_icon="🔐",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "🔐 Social Media Privacy Risk Assessment"
)

st.markdown(
    """
    ### Privacy Self-Assessment

    Answer the questions below based on your current
    social-media settings and online-sharing habits.

    The system analyzes multiple privacy dimensions and
    generates a personalized privacy-risk assessment.
    """
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_predictor():

    return PrivacyRiskPredictor()


try:

    predictor = load_predictor()

except FileNotFoundError as error:

    st.error(str(error))

    st.stop()


# ============================================================
# HELPER
# ============================================================

def yes_no_question(
    question,
    default="No"
):

    return st.radio(
        question,
        ["No", "Yes"],
        index=(
            1
            if default == "Yes"
            else 0
        ),
        horizontal=True
    ) == "Yes"


# ============================================================
# QUESTIONNAIRE
# ============================================================

st.header("📝 Privacy Questionnaire")


# ============================================================
# SECTION 1
# ============================================================

with st.expander(
    "1️⃣ Profile & Personal Information",
    expanded=True
):

    col1, col2 = st.columns(2)

    with col1:

        profile_public = yes_no_question(
            "Q1. Is your profile information publicly visible?"
        )

        location_shared = yes_no_question(
            "Q2. Do you publicly share your location?"
        )

        phone_shared = yes_no_question(
            "Q3. Is your phone number visible on your profile?"
        )

        email_shared = yes_no_question(
            "Q4. Is your personal email publicly visible?"
        )

        date_of_birth_shared = yes_no_question(
            "Q5. Is your date of birth publicly visible?"
        )

    with col2:

        workplace_shared = yes_no_question(
            "Q6. Is your workplace publicly visible?"
        )

        education_shared = yes_no_question(
            "Q7. Is your school/college information public?"
        )

        relationship_status_shared = yes_no_question(
            "Q8. Is your relationship status publicly visible?"
        )

        family_information_shared = yes_no_question(
            "Q9. Do you publicly share information about family members?"
        )


# ============================================================
# SECTION 2
# ============================================================

with st.expander(
    "2️⃣ Followers & Social Exposure"
):

    col1, col2 = st.columns(2)

    with col1:

        account_public = yes_no_question(
            "Q10. Is your social-media account public?"
        )

        accepts_unknown_requests = yes_no_question(
            "Q11. Do you accept friend/follow requests from people you do not know?"
        )

        public_friend_list = yes_no_question(
            "Q12. Is your friend/follower list publicly visible?"
        )

    with col2:

        public_interactions = yes_no_question(
            "Q13. Can other people publicly see your likes/comments/interactions?"
        )

        unknown_followers = st.number_input(
            "Q14. Approximately how many followers do you not personally know?",
            min_value=0,
            max_value=100000,
            value=20,
            step=1
        )


# ============================================================
# SECTION 3
# ============================================================

with st.expander(
    "3️⃣ Posts, Photos & Content Sharing"
):

    col1, col2 = st.columns(2)

    with col1:

        location_posts = yes_no_question(
            "Q15. Do you post your current or recent location?"
        )

        geotagging_enabled = yes_no_question(
            "Q16. Do you use location/geotagging on posts?"
        )

        travel_plans_shared = yes_no_question(
            "Q17. Do you publicly share upcoming travel plans?"
        )

        sensitive_posts = yes_no_question(
            "Q18. Do your posts sometimes contain sensitive personal information?"
        )

        photos_public = yes_no_question(
            "Q19. Are most of your photos publicly visible?"
        )

    with col2:

        stories_public = yes_no_question(
            "Q20. Are your stories visible to a broad audience?"
        )

        external_links_shared = yes_no_question(
            "Q21. Do you frequently share external links on your profile?"
        )

        oversharing_personal_information = yes_no_question(
            "Q22. Do you frequently share personal details online?"
        )

        posts_per_week = st.number_input(
            "Q23. Approximately how many posts do you make per week?",
            min_value=0,
            max_value=500,
            value=10,
            step=1
        )


# ============================================================
# SECTION 4
# ============================================================

with st.expander(
    "4️⃣ Account Security"
):

    col1, col2 = st.columns(2)

    with col1:

        two_factor_auth = yes_no_question(
            "Q24. Is two-factor authentication enabled?"
        )

        login_alerts_enabled = yes_no_question(
            "Q25. Are login/security alerts enabled?"
        )

        password_reused = yes_no_question(
            "Q26. Do you reuse your social-media password on other websites?"
        )

    with col2:

        unknown_login_detected = yes_no_question(
            "Q27. Have you noticed an unfamiliar login or session?"
        )


# ============================================================
# SECTION 5
# ============================================================

with st.expander(
    "5️⃣ Third-Party Applications"
):

    col1, col2 = st.columns(2)

    with col1:

        third_party_apps = st.number_input(
            "Q28. Approximately how many third-party applications have social-account access?",
            min_value=0,
            max_value=100,
            value=2,
            step=1
        )

        old_unused_apps = yes_no_question(
            "Q29. Do old or unused applications still have account access?"
        )

    with col2:

        connects_social_account_to_other_apps = yes_no_question(
            "Q30. Do you connect your social-media account to other apps or websites?"
        )


# ============================================================
# BUILD INPUT
# ============================================================

input_data = {

    "profile_public":
        int(profile_public),

    "account_public":
        int(account_public),

    "location_shared":
        int(location_shared),

    "phone_shared":
        int(phone_shared),

    "email_shared":
        int(email_shared),

    "date_of_birth_shared":
        int(date_of_birth_shared),

    "workplace_shared":
        int(workplace_shared),

    "education_shared":
        int(education_shared),

    "relationship_status_shared":
        int(relationship_status_shared),

    "family_information_shared":
        int(family_information_shared),

    "unknown_followers":
        unknown_followers,

    "third_party_apps":
        third_party_apps,

    "posts_per_week":
        posts_per_week,

    "accepts_unknown_requests":
        int(accepts_unknown_requests),

    "public_friend_list":
        int(public_friend_list),

    "public_interactions":
        int(public_interactions),

    "location_posts":
        int(location_posts),

    "geotagging_enabled":
        int(geotagging_enabled),

    "travel_plans_shared":
        int(travel_plans_shared),

    "sensitive_posts":
        int(sensitive_posts),

    "photos_public":
        int(photos_public),

    "stories_public":
        int(stories_public),

    "external_links_shared":
        int(external_links_shared),

    "oversharing_personal_information":
        int(oversharing_personal_information),

    "two_factor_auth":
        int(two_factor_auth),

    "login_alerts_enabled":
        int(login_alerts_enabled),

    "password_reused":
        int(password_reused),

    "unknown_login_detected":
        int(unknown_login_detected),

    "old_unused_apps":
        int(old_unused_apps),

    "connects_social_account_to_other_apps":
        int(connects_social_account_to_other_apps)
}


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.divider()

if st.button(
    "🔍 Analyze My Privacy Risk",
    use_container_width=True,
    type="primary"
):

    try:

        result = predictor.predict(
            input_data
        )

        st.success(
            "Privacy assessment completed successfully."
        )

        # ====================================================
        # MAIN METRICS
        # ====================================================

        st.header("📊 Overall Assessment")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "ML Prediction",
                result["model_prediction"]
            )

        with col2:

            st.metric(
                "Risk Level",
                result["risk_level"]
            )

        with col3:

            st.metric(
                "Exposure Score",
                result["exposure_score"]
            )

        with col4:

            highest_probability = max(
                result["probabilities"].values()
            )

            st.metric(
                "Prediction Confidence",
                f"{highest_probability * 100:.1f}%"
            )


        # ====================================================
        # CATEGORY ANALYSIS
        # ====================================================

        st.header(
            "📈 Privacy Category Analysis"
        )

        category_scores = result[
            "category_scores"
        ]

        st.bar_chart(
            category_scores
        )


        # ====================================================
        # PROBABILITIES
        # ====================================================

        st.subheader(
            "🤖 ML Risk Probabilities"
        )

        st.bar_chart(
            result["probabilities"]
        )


        # ====================================================
        # DETAILED SCORES
        # ====================================================

        st.subheader(
            "🔎 Detailed Analysis"
        )

        for category, score in category_scores.items():

            st.write(
                f"**{category}: {score}**"
            )

            if category == "Personal Data Exposure":

                maximum = 17

            elif category == "Account Security":

                maximum = 16

            elif category == "Social Exposure":

                maximum = 14

            elif category == "Content Sharing":

                maximum = 22

            else:

                maximum = 8

            progress = min(
                score / maximum,
                1.0
            )

            st.progress(
                progress
            )


        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.header(
            "🛡️ Personalized Recommendations"
        )

        recommendations = result[
            "recommendations"
        ]

        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):

            st.warning(
                f"{index}. {recommendation}"
            )


        # ====================================================
        # QUESTION SUMMARY
        # ====================================================

        st.header(
            "📋 Assessment Summary"
        )

        yes_answers = sum(
            value == 1
            for value in input_data.values()
            if isinstance(value, int)
        )

        total_binary_questions = sum(
            isinstance(value, int)
            for value in input_data.values()
        )

        st.write(
            f"You answered **Yes** to approximately "
            f"**{yes_answers}** out of "
            f"**{total_binary_questions}** binary privacy/security questions."
        )

        st.info(
            "This assessment analyzes privacy exposure based on the "
            "answers provided. It is an educational risk-assessment "
            "tool and is not a formal security audit."
        )

    except Exception as error:

        st.error(
            f"Prediction failed: {error}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Social Media Privacy Risk Assessment | "
    "Educational ML-based privacy analysis system"
)