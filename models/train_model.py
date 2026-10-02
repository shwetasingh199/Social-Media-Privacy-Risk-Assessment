import os
import sys

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    accuracy_score,
    f1_score,
    confusion_matrix
)


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from services.feature_engine import (
    extract_privacy_features,
    get_model_features
)


DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "privacy_risk_dataset.csv"
)

MODEL_DIR = os.path.join(
    PROJECT_ROOT,
    "models_saved"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "privacy_risk_model.pkl"
)


def train():

    print("=" * 60)
    print("LOADING DATASET")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH)

    df_features = extract_privacy_features(
        df
    )

    feature_columns = get_model_features()

    X = df_features[
        feature_columns
    ]

    y = df_features[
        "risk_level"
    ]

    print(f"Dataset shape: {df.shape}")
    print(f"Number of model features: {len(feature_columns)}")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = Pipeline([
        (
            "scaler",
            StandardScaler()
        ),

        (
            "classifier",
            RandomForestClassifier(
                n_estimators=250,
                max_depth=12,
                min_samples_split=5,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1
            )
        )
    ])

    print("\nTraining model...")

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print("\n" + "=" * 60)
    print("MODEL PERFORMANCE")
    print("=" * 60)

    print(
        f"Accuracy: {accuracy:.4f}"
    )

    print(
        f"Weighted F1: {f1:.4f}"
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    os.makedirs(
        MODEL_DIR,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print("\n" + "=" * 60)
    print("MODEL SAVED SUCCESSFULLY")
    print("=" * 60)

    print(MODEL_PATH)


if __name__ == "__main__":
    train()