# 🔐 Social Media Privacy Risk Assessment

An **ML-powered Social Media Privacy Risk Assessment System** that evaluates a user's privacy exposure through a comprehensive **30-question privacy questionnaire**. The system combines feature engineering, rule-based risk analysis, machine learning classification, category-level analysis, and personalized privacy recommendations in an interactive Streamlit dashboard.

---

## 📌 Overview

Social media platforms involve continuous sharing of personal information, location data, photos, interactions, third-party application access, and account activity.

This project provides an educational and analytical system that helps users understand their potential privacy exposure based on their online-sharing habits and security settings.

The application collects questionnaire responses and transforms them into privacy-related features. These features are analyzed across multiple dimensions and passed to a trained **Random Forest classification model** to predict an overall privacy risk category.

### Key Analysis Areas

* 👤 Personal Data Exposure
* 🔐 Account Security
* 👥 Social Exposure
* 📱 Content Sharing
* 🔗 Third-Party Application Risk
* 📊 Overall Privacy Exposure
* 🤖 Machine Learning Risk Prediction
* 🛡️ Personalized Recommendations
  
---

## Screenshots

<img width="1858" height="898" alt="P2 O s1" src="https://github.com/user-attachments/assets/672ead41-e6dc-4828-b406-65dac94819ab" />
<img width="1858" height="890" alt="P2 O s2" src="https://github.com/user-attachments/assets/30a9a8ce-8ad8-445d-9730-de2b6e5be870" />
<img width="1855" height="867" alt="P2 O s3" src="https://github.com/user-attachments/assets/f5e3abe1-634e-4cca-accd-aec09e1633b5" />
<img width="1883" height="637" alt="P2 O s4" src="https://github.com/user-attachments/assets/07aa0ba7-f22e-4c6d-b9ba-c655169800c1" />
<img width="1787" height="633" alt="P2 O s5" src="https://github.com/user-attachments/assets/c595f0f9-f399-4bfd-90f6-bdb7c5be4b89" />
<img width="1882" height="865" alt="P2 O s6" src="https://github.com/user-attachments/assets/8f469253-b6a1-4b46-874b-be6abe1c8fbd" />
<img width="1835" height="841" alt="P2 O s7" src="https://github.com/user-attachments/assets/92c0b1c5-687c-438d-a1a6-7ed47fc1934a" />

---

## ✨ Key Features

### 📝 30-Question Privacy Questionnaire

The application collects structured responses covering:

* Public profile visibility
* Account visibility
* Location sharing
* Phone number exposure
* Email exposure
* Date of birth visibility
* Workplace information
* Education information
* Relationship status
* Family information
* Unknown followers
* Unknown friend/follow requests
* Public friend/follower lists
* Public interactions
* Location-based posts
* Geotagging
* Travel plans
* Sensitive information in posts
* Public photos
* Public stories
* External links
* Personal-information oversharing
* Two-factor authentication
* Login alerts
* Password reuse
* Unknown login activity
* Third-party applications
* Unused application access
* Social-account connections to other applications

---

## 🧠 Machine Learning

The project uses a **Random Forest Classifier** to classify privacy risk into four categories:

```text
Low
Medium
High
Critical
```

### ML Pipeline

```text
User Questionnaire
        ↓
Raw Privacy Data
        ↓
Feature Engineering
        ↓
Privacy Category Scores
        ↓
Random Forest Classifier
        ↓
Risk Prediction
        ↓
Personalized Recommendations
```

The model uses engineered privacy and security features rather than directly relying only on raw questionnaire responses.

---

## 📊 Privacy Analysis Dimensions

### 1. Personal Data Exposure

Evaluates exposure of:

* Phone number
* Email
* Location
* Date of birth
* Workplace
* Education
* Relationship information
* Family information

### 2. Account Security

Evaluates:

* Two-factor authentication
* Login alerts
* Password reuse
* Unknown login activity
* Account visibility

### 3. Social Exposure

Evaluates:

* Unknown followers
* Unknown friend requests
* Public follower/friend lists
* Public interactions
* Account visibility

### 4. Content Sharing Risk

Evaluates:

* Location posts
* Geotagging
* Travel plans
* Sensitive posts
* Public photos
* Public stories
* External links
* Oversharing
* Posting frequency

### 5. Application Risk

Evaluates:

* Number of third-party applications
* Unused application access
* Connected applications and websites

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────────────┐
                    │   Streamlit Dashboard    │
                    │  30-Question Assessment  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    Input Validation       │
                    │   Questionnaire Data     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    Feature Engineering   │
                    │      feature_engine.py   │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       Personal Data       Account Security    Social Exposure
           Score                Score                Score
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │     Content Risk         │
                    │   Application Risk       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │ Overall Privacy Exposure │
                    │          Score           │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │  Random Forest Classifier│
                    └────────────┬─────────────┘
                                 │
                 ┌───────────────┴────────────────┐
                 ▼                                ▼
        Risk Prediction                  Risk Probabilities
                 │                                │
                 └───────────────┬────────────────┘
                                 ▼
                    ┌──────────────────────────┐
                    │ Personalized Privacy     │
                    │ Recommendations          │
                    └──────────────────────────┘
```

---

## 📁 Project Structure

```text
Social-Media-Privacy-Risk-Assessment/
│
├── app/
│   ├── __init__.py
│   └── streamlit_app.py
│
├── data/
│   ├── __init__.py
│   └── generate_dataset.py
│
├── models/
│   ├── __init__.py
│   └── train_model.py
│
├── services/
│   ├── __init__.py
│   ├── feature_engine.py
│   ├── predictor.py
│   └── risk_engine.py
│
├── tests/
│   ├── __init__.py
│   └── test_features.py
│
├── models_saved/
│   └── privacy_risk_model.pkl
│
├── data/
│   └── privacy_risk_dataset.csv
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.py
```

> **Note:** The generated dataset and trained model are excluded from Git using `.gitignore`. They can be regenerated locally.

---

## 🛠️ Technology Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| Pandas        | Data processing           |
| NumPy         | Numerical computation     |
| Scikit-learn  | Machine learning          |
| Random Forest | Risk classification       |
| Joblib        | Model serialization       |
| Streamlit     | Interactive web dashboard |
| Pytest        | Automated testing         |
| Git & GitHub  | Version control           |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Social-Media-Privacy-Risk-Assessment.git
```

### 2. Open the Project

```bash
cd Social-Media-Privacy-Risk-Assessment
```

### 3. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

### 4. Activate the Environment

```powershell
.\venv\Scripts\activate
```

### 5. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1 — Generate the Dataset

```powershell
python -m data.generate_dataset
```

This creates:

```text
data/privacy_risk_dataset.csv
```

The project uses synthetic data for development and demonstration.

---

### Step 2 — Train the Model

```powershell
python -m models.train_model
```

The trained model is saved as:

```text
models_saved/privacy_risk_model.pkl
```

The training process displays:

* Accuracy
* Weighted F1 Score
* Classification Report
* Confusion Matrix

---

### Step 3 — Run Tests

```powershell
pytest
```

The test suite validates the feature-engineering pipeline and privacy-score generation.

---

### Step 4 — Launch the Dashboard

```powershell
streamlit run app/streamlit_app.py
```

The application will open in your browser.

---

## 🚀 One-Command Execution

The project also includes `run.py`.

Run:

```powershell
python run.py
```

This automatically:

```text
Generate Dataset
       ↓
Train Model
       ↓
Launch Streamlit Dashboard
```

---

## 📊 Dashboard Workflow

The user completes the questionnaire through five sections:

```text
1. Profile & Personal Information
              ↓
2. Followers & Social Exposure
              ↓
3. Posts, Photos & Content Sharing
              ↓
4. Account Security
              ↓
5. Third-Party Applications
              ↓
       Analyze My Privacy Risk
```

The dashboard then displays:

* ML risk prediction
* Overall risk level
* Exposure score
* Prediction confidence
* Privacy category scores
* ML risk probabilities
* Detailed analysis
* Personalized recommendations
* Questionnaire summary

---

## 🔍 Example Output

A typical assessment may produce:

```text
Overall Assessment

ML Prediction: HIGH
Risk Level: HIGH
Exposure Score: 27
Prediction Confidence: 91.4%
```

Category analysis:

```text
Personal Data Exposure
Account Security
Social Exposure
Content Sharing
Application Risk
```

The application also provides recommendations based on the user's specific answers.

---

## 🧪 Testing

Run the complete test suite using:

```powershell
pytest
```

Example:

```text
======================== test session starts ========================

tests/test_features.py ...

========================= 3 passed =========================
```

Testing covers:

* Feature generation
* Profile completeness
* Privacy exposure score generation

---

## 🔐 Privacy & Security

This project is designed as an educational privacy-risk assessment tool.

### Important principles

* No real social-media credentials are required.
* No social-media API access is required.
* No real user account data is collected.
* The demonstration dataset is synthetic.
* Questionnaire responses are processed locally.
* No passwords or authentication credentials are requested.

The system should not be considered a replacement for a professional cybersecurity or privacy audit.

---

## 📌 Dataset

The project generates a synthetic dataset containing privacy-related behavioral and security variables.

The generated dataset includes features related to:

```text
Profile visibility
Account visibility
Personal information
Location sharing
Followers
Posting behavior
Content sharing
Account security
Third-party applications
Privacy exposure
```

The dataset is generated using controlled synthetic distributions and is intended for educational machine-learning experimentation.

---

## 🧩 Feature Engineering

The feature-engineering module converts questionnaire responses into meaningful analytical features.

Examples include:

```text
personal_data_score
security_score
social_exposure_score
content_risk_score
application_risk_score
profile_completeness
privacy_exposure_score
```

These engineered features allow the application to analyze privacy exposure across multiple dimensions.

---

## 🤖 Model Details

### Algorithm

```text
Random Forest Classifier
```

### Configuration

```text
n_estimators = 250
max_depth = 12
min_samples_split = 5
class_weight = balanced
random_state = 42
```

The model is trained using a stratified train-test split.

### Evaluation Metrics

The training pipeline reports:

* Accuracy
* Weighted F1 Score
* Precision
* Recall
* Classification Report
* Confusion Matrix

---

## 🛡️ Recommendation Engine

The recommendation engine converts detected privacy concerns into actionable suggestions.

Examples include:

```text
Enable two-factor authentication.

Avoid publicly sharing precise location.

Review unknown followers.

Disable unnecessary geotagging.

Remove unused third-party applications.

Limit public visibility of personal information.

Review recent account-login activity.
```

Recommendations are generated based on the user's questionnaire responses.

---

## 🧪 Example Use Cases

This project can be used for:

* Cybersecurity education
* Privacy-awareness demonstrations
* Machine-learning portfolio development
* Data-science projects
* Security analytics
* Privacy-risk research
* Student academic projects
* ML classification demonstrations
* Interactive Streamlit dashboards

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python development
* Data generation
* Data preprocessing
* Feature engineering
* Classification
* Random Forest
* Model evaluation
* Risk scoring
* Rule-based recommendation systems
* Streamlit application development
* Automated testing
* Modular project architecture
* Git and GitHub
* Privacy and security concepts

---

## 🔮 Future Enhancements

Possible future improvements include:

* Explainable AI using SHAP
* Feature-importance visualization
* PDF privacy reports
* User authentication
* Database integration
* Historical assessment tracking
* Privacy-score comparison over time
* Interactive risk trends
* More ML algorithms
* Model comparison
* Cross-validation
* API deployment using FastAPI
* Cloud deployment
* Role-based access control
* Privacy-policy analysis
* Natural-language privacy recommendations

---

## ⚠️ Disclaimer

This application is intended for **educational and informational purposes only**.

The privacy-risk results are based on the information provided by the user and the synthetic machine-learning model used in this project. The results do not constitute a professional cybersecurity assessment, legal advice, or a definitive measurement of real-world privacy or security risk.

Users should independently review the privacy and security settings of the platforms they use.

---

## 👩‍💻 Author

**Shweta Singh**

B.Tech — Electronics & Communication Engineering

Interested in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Business Analytics
* Cybersecurity & Privacy
* Cloud Computing

---

## ⭐ Support

If you find this project useful for learning or academic purposes, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and portfolio purposes.

You may modify and extend the project for learning, experimentation, and academic use.
