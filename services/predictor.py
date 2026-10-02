import os

import joblib
import pandas as pd

from services.feature_engine import (
    extract_privacy_features
)

from services.risk_engine import (
    calculate_risk_level,
    generate_recommendations
)


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models_saved",
    "privacy_risk_model.pkl"
)


class PrivacyRiskPredictor:

    def __init__(self):

        if not os.path.exists(MODEL_PATH):

            raise FileNotFoundError(
                "Trained model not found. "
                "Run: python -m models.train_model"
            )

        self.model = joblib.load(
            MODEL_PATH
        )

    def predict(self, input_data):

        df = pd.DataFrame(
            [input_data]
        )

        df_features = extract_privacy_features(
            df
        )

        prediction = self.model.predict(
            df_features
        )[0]

        probabilities = self.model.predict_proba(
            df_features
        )[0]

        classes = self.model.classes_

        probability_dict = {
            class_name: float(probability)
            for class_name, probability
            in zip(
                classes,
                probabilities
            )
        }

        exposure_score = float(
            df_features[
                "privacy_exposure_score"
            ].iloc[0]
        )

        risk_level = calculate_risk_level(
            exposure_score
        )

        recommendations = generate_recommendations(
            df.iloc[0]
        )

        category_scores = {

            "Personal Data Exposure":
                int(
                    df_features[
                        "personal_data_score"
                    ].iloc[0]
                ),

            "Account Security":
                int(
                    df_features[
                        "security_score"
                    ].iloc[0]
                ),

            "Social Exposure":
                int(
                    df_features[
                        "social_exposure_score"
                    ].iloc[0]
                ),

            "Content Sharing":
                int(
                    df_features[
                        "content_risk_score"
                    ].iloc[0]
                ),

            "Application Risk":
                int(
                    df_features[
                        "application_risk_score"
                    ].iloc[0]
                )
        }

        return {

            "model_prediction":
                prediction,

            "risk_level":
                risk_level,

            "exposure_score":
                round(
                    exposure_score,
                    2
                ),

            "probabilities":
                probability_dict,

            "category_scores":
                category_scores,

            "recommendations":
                recommendations
        }