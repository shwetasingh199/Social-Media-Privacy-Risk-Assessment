import os
import sys

import pandas as pd


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from services.feature_engine import (
    extract_privacy_features
)


def create_test_data():

    return pd.DataFrame([
        {

            "profile_public": 1,
            "account_public": 1,

            "location_shared": 1,
            "phone_shared": 1,
            "email_shared": 1,
            "date_of_birth_shared": 1,
            "workplace_shared": 1,
            "education_shared": 1,
            "relationship_status_shared": 1,
            "family_information_shared": 1,

            "unknown_followers": 100,
            "third_party_apps": 5,
            "posts_per_week": 20,

            "accepts_unknown_requests": 1,
            "public_friend_list": 1,
            "public_interactions": 1,

            "location_posts": 1,
            "geotagging_enabled": 1,
            "travel_plans_shared": 1,
            "sensitive_posts": 1,
            "photos_public": 1,
            "stories_public": 1,
            "external_links_shared": 1,
            "oversharing_personal_information": 1,

            "two_factor_auth": 0,
            "login_alerts_enabled": 0,
            "password_reused": 1,
            "unknown_login_detected": 1,

            "old_unused_apps": 1,
            "connects_social_account_to_other_apps": 1
        }
    ])


def test_feature_generation():

    df = create_test_data()

    result = extract_privacy_features(
        df
    )

    expected_features = [

        "profile_completeness",

        "personal_data_score",

        "security_score",

        "social_exposure_score",

        "content_risk_score",

        "application_risk_score",

        "privacy_exposure_score"
    ]

    for feature in expected_features:

        assert feature in result.columns


def test_profile_completeness():

    df = create_test_data()

    result = extract_privacy_features(
        df
    )

    assert (
        result[
            "profile_completeness"
        ].iloc[0]
        == 1.0
    )


def test_privacy_score_exists():

    df = create_test_data()

    result = extract_privacy_features(
        df
    )

    assert (
        result[
            "privacy_exposure_score"
        ].iloc[0]
        > 0
    )