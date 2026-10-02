import os
import sys

import numpy as np
import pandas as pd


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from services.feature_engine import extract_privacy_features


np.random.seed(42)


def generate_dataset(n_samples=3000):

    data = []

    for i in range(n_samples):

        data.append({

            "user_id": f"USER_{i + 1:05d}",

            # Profile
            "profile_public": np.random.binomial(1, 0.55),
            "account_public": np.random.binomial(1, 0.55),

            "location_shared": np.random.binomial(1, 0.40),
            "phone_shared": np.random.binomial(1, 0.25),
            "email_shared": np.random.binomial(1, 0.40),
            "date_of_birth_shared": np.random.binomial(1, 0.35),
            "workplace_shared": np.random.binomial(1, 0.45),
            "education_shared": np.random.binomial(1, 0.50),
            "relationship_status_shared": np.random.binomial(1, 0.30),
            "family_information_shared": np.random.binomial(1, 0.25),

            # Social exposure
            "unknown_followers": np.random.poisson(45),
            "third_party_apps": np.random.poisson(3),
            "posts_per_week": np.random.poisson(10),

            "accepts_unknown_requests": np.random.binomial(
                1, 0.35
            ),

            "public_friend_list": np.random.binomial(
                1, 0.40
            ),

            "public_interactions": np.random.binomial(
                1, 0.45
            ),

            # Content
            "location_posts": np.random.binomial(
                1, 0.30
            ),

            "geotagging_enabled": np.random.binomial(
                1, 0.25
            ),

            "travel_plans_shared": np.random.binomial(
                1, 0.25
            ),

            "sensitive_posts": np.random.binomial(
                1, 0.20
            ),

            "photos_public": np.random.binomial(
                1, 0.55
            ),

            "stories_public": np.random.binomial(
                1, 0.50
            ),

            "external_links_shared": np.random.binomial(
                1, 0.30
            ),

            "oversharing_personal_information": np.random.binomial(
                1, 0.25
            ),

            # Security
            "two_factor_auth": np.random.binomial(
                1, 0.55
            ),

            "login_alerts_enabled": np.random.binomial(
                1, 0.60
            ),

            "password_reused": np.random.binomial(
                1, 0.35
            ),

            "unknown_login_detected": np.random.binomial(
                1, 0.12
            ),

            # Applications
            "old_unused_apps": np.random.binomial(
                1, 0.30
            ),

            "connects_social_account_to_other_apps": np.random.binomial(
                1, 0.35
            )
        })

    df = pd.DataFrame(data)

    # Generate engineered features
    df = extract_privacy_features(df)

    # ========================================================
    # CREATE SYNTHETIC RISK LABEL
    # ========================================================

    raw_score = (
        df["privacy_exposure_score"]
        + df["account_public"] * 2
        + df["profile_public"] * 1
    )

    noise = np.random.normal(
        loc=0,
        scale=2.0,
        size=len(df)
    )

    raw_score = raw_score + noise

    conditions = [
        raw_score < 10,
        raw_score < 20,
        raw_score < 35
    ]

    choices = [
        "Low",
        "Medium",
        "High"
    ]

    df["risk_level"] = np.select(
        conditions,
        choices,
        default="Critical"
    )

    # ========================================================
    # RAW DATASET COLUMNS
    # ========================================================

    output_columns = [
        "user_id",

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

        "risk_level"
    ]

    return df[output_columns]


if __name__ == "__main__":

    output_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    output_path = os.path.join(
        output_dir,
        "privacy_risk_dataset.csv"
    )

    df = generate_dataset()

    df.to_csv(
        output_path,
        index=False
    )

    print("=" * 60)
    print("PRIVACY RISK DATASET GENERATED")
    print("=" * 60)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print(f"\nSaved to:")
    print(output_path)

    print("\nRisk distribution:")
    print(
        df["risk_level"].value_counts()
    )