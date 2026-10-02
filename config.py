import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    str(BASE_DIR / "privacy_assessment.db")
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "development-only-change-this-secret"
)

DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

MAX_CONTENT_LENGTH = 1024 * 1024

RISK_WEIGHTS = {
    "profile_exposure": 0.10,
    "personal_information": 0.15,
    "location_exposure": 0.15,
    "content_exposure": 0.10,
    "connection_risk": 0.10,
    "tagging_risk": 0.05,
    "account_security": 0.15,
    "third_party_apps": 0.05,
    "social_engineering": 0.10,
    "digital_footprint": 0.05,
}

RISK_THRESHOLDS = {
    "LOW": (0, 20),
    "MODERATE": (21, 40),
    "HIGH": (41, 70),
    "CRITICAL": (71, 100),
}