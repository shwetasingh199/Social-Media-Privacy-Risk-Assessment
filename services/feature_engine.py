import pandas as pd


# ============================================================
# PERSONAL DATA EXPOSURE
# ============================================================

def calculate_personal_data_score(row):
    score = 0

    score += int(row["location_shared"]) * 2
    score += int(row["phone_shared"]) * 3
    score += int(row["email_shared"]) * 2
    score += int(row["date_of_birth_shared"]) * 3
    score += int(row["workplace_shared"]) * 2
    score += int(row["education_shared"]) * 1
    score += int(row["relationship_status_shared"]) * 2
    score += int(row["family_information_shared"]) * 2

    return score


# ============================================================
# ACCOUNT SECURITY
# ============================================================

def calculate_security_score(row):
    score = 0

    if row["two_factor_auth"] == 0:
        score += 4

    if row["login_alerts_enabled"] == 0:
        score += 2

    if row["password_reused"] == 1:
        score += 4

    if row["unknown_login_detected"] == 1:
        score += 4

    if row["account_public"] == 1:
        score += 2

    return score


# ============================================================
# SOCIAL EXPOSURE
# ============================================================

def calculate_social_exposure_score(row):
    score = 0

    if row["account_public"] == 1:
        score += 3

    if row["unknown_followers"] > 100:
        score += 4
    elif row["unknown_followers"] > 50:
        score += 3
    elif row["unknown_followers"] > 20:
        score += 1

    if row["accepts_unknown_requests"] == 1:
        score += 3

    if row["public_friend_list"] == 1:
        score += 2

    if row["public_interactions"] == 1:
        score += 2

    return score


# ============================================================
# CONTENT SHARING RISK
# ============================================================

def calculate_content_risk_score(row):
    score = 0

    if row["location_posts"] == 1:
        score += 3

    if row["geotagging_enabled"] == 1:
        score += 3

    if row["travel_plans_shared"] == 1:
        score += 2

    if row["sensitive_posts"] == 1:
        score += 4

    if row["photos_public"] == 1:
        score += 2

    if row["stories_public"] == 1:
        score += 1

    if row["external_links_shared"] == 1:
        score += 2

    if row["oversharing_personal_information"] == 1:
        score += 3

    if row["posts_per_week"] > 20:
        score += 2
    elif row["posts_per_week"] > 10:
        score += 1

    return score


# ============================================================
# APPLICATION / PLATFORM RISK
# ============================================================

def calculate_application_risk_score(row):
    score = 0

    if row["third_party_apps"] > 5:
        score += 4
    elif row["third_party_apps"] > 2:
        score += 2
    elif row["third_party_apps"] > 0:
        score += 1

    if row["old_unused_apps"] == 1:
        score += 2

    if row["connects_social_account_to_other_apps"] == 1:
        score += 2

    return score


# ============================================================
# PROFILE COMPLETENESS
# ============================================================

def calculate_profile_completeness(row):
    fields = [
        "profile_public",
        "location_shared",
        "phone_shared",
        "email_shared",
        "date_of_birth_shared",
        "workplace_shared",
        "education_shared",
        "relationship_status_shared",
        "family_information_shared"
    ]

    available = sum(
        int(row[field])
        for field in fields
    )

    return available / len(fields)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

def extract_privacy_features(df):

    df = df.copy()

    df["profile_completeness"] = df.apply(
        calculate_profile_completeness,
        axis=1
    )

    df["personal_data_score"] = df.apply(
        calculate_personal_data_score,
        axis=1
    )

    df["security_score"] = df.apply(
        calculate_security_score,
        axis=1
    )

    df["social_exposure_score"] = df.apply(
        calculate_social_exposure_score,
        axis=1
    )

    df["content_risk_score"] = df.apply(
        calculate_content_risk_score,
        axis=1
    )

    df["application_risk_score"] = df.apply(
        calculate_application_risk_score,
        axis=1
    )

    # Overall privacy exposure
    df["privacy_exposure_score"] = (
        df["personal_data_score"]
        + df["security_score"]
        + df["social_exposure_score"]
        + df["content_risk_score"]
        + df["application_risk_score"]
    )

    # Keep score within a readable range
    df["privacy_exposure_score"] = (
        df["privacy_exposure_score"]
        .clip(0, 50)
    )

    return df


# ============================================================
# MODEL FEATURES
# ============================================================

def get_model_features():

    return [
        "profile_public",
        "account_public",
        "location_shared",
        "phone_shared",
        "email_shared",
        "date_of_birth_shared",
        "workplace_shared",
        "education_shared",
        "relationship_status_shared",
        "family_information_shared",

        "unknown_followers",
        "third_party_apps",
        "posts_per_week",

        "accepts_unknown_requests",
        "public_friend_list",
        "public_interactions",

        "location_posts",
        "geotagging_enabled",
        "travel_plans_shared",
        "sensitive_posts",
        "photos_public",
        "stories_public",
        "external_links_shared",
        "oversharing_personal_information",

        "two_factor_auth",
        "login_alerts_enabled",
        "password_reused",
        "unknown_login_detected",

        "old_unused_apps",
        "connects_social_account_to_other_apps",

        "profile_completeness",
        "personal_data_score",
        "security_score",
        "social_exposure_score",
        "content_risk_score",
        "application_risk_score",
        "privacy_exposure_score"
    ]