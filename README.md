## Student-Burnout-Dropout-Risk

AI-powered behavioural analytics system that predicts student burnout risk, disengagement, and dropout probability using explainable ML and recommends early intervention strategies.

## 📖 Abstract

Student burnout and academic disengagement are major contributors to increasing dropout rates in higher education institutions. Traditional monitoring approaches often identify problems only after academic performance significantly declines, limiting the effectiveness of intervention strategies.

This project presents an **AI-driven behavioural analytics framework** capable of predicting student burnout risk, academic disengagement indicators, and dropout probability using behavioural signals such as attendance trends, LMS activity simulation, assignment submission delays, and feedback sentiment patterns.

The system combines:

- Machine Learning Prediction Models
- Explainable Artificial Intelligence (SHAP)
- Behavioural Trigger Identification
- Intervention Recommendation Engine
- Faculty Early Warning Dashboard

The primary objective is to enable **proactive faculty support systems that improve student engagement and retention outcomes**.

---

## 🚨 Problem Statement

Universities currently lack intelligent systems capable of detecting early behavioural warning signals associated with student burnout and disengagement.

Common early indicators include:

- Reduced LMS login frequency
- Increased assignment submission delays
- Attendance decline
- Negative feedback sentiment
- Irregular activity patterns

Without early intervention:

- Academic stress increases.
- Student motivation decreases.
- Dropout probability rises.

The challenge is to design a predictive system capable of identifying these behavioural risks before academic failure occurs.

---

## 🎯 Objectives

- Predict Burnout Risk Level (Low / Medium / High).
- Estimate student Dropout Probability.
- Detect Academic Disengagement behaviour.
- Identify key behavioural triggers influencing predictions.
- Recommend faculty intervention strategies.
- Provide institutional-level analytics visualization.

---

## 🧠 System Architecture

Behavioural Dataset Simulation  
↓  
Data Preprocessing and Cleaning  
↓  
Feature Engineering and Behaviour Modelling  
↓  
Machine Learning Model Training (Random Forest Classifier)  
↓  
Burnout Risk Prediction Engine  
↓  
Explainable AI Analysis (SHAP)  
↓  
Behavioural Trigger Identification  
↓  
Intervention Recommendation Engine  
↓  
Faculty Decision Support Dashboard

---

## ⚙️ Workflow

Dataset Simulation → Preprocessing → Feature Selection → Model Training → Risk Prediction → Explainability Analysis → Alert Detection → Dashboard Visualization

---

## 🧪 Methodology

### Dataset Simulation

Synthetic behavioural datasets were generated to simulate realistic university environments.

Key behavioural attributes include:

- Attendance Percentage
- LMS Login Frequency (simulated)
- Assignment Submission Delay
- Feedback Sentiment Score
- Activity Pattern Irregularity

Datasets used:

- student_burnout_dataset.csv
- student_burnout_dataset_with_actions.csv

The use of synthetic datasets ensures privacy preservation and ethical experimentation.

---

### Data Preprocessing

The preprocessing pipeline includes:

- Missing value handling.
- Label encoding of categorical variables.
- Behavioural feature normalization.

Burnout categories were encoded as:

Low → 0  
Medium → 1  
High → 2

---

### Feature Engineering

Behavioural indicators selected include:

- Attendance Percentage
- Burnout Risk Score
- Dropout Probability

Derived indicators:

- Academic Disengagement Detection.
- Behaviour Irregularity Score.

These features represent behavioural engagement patterns rather than academic grades alone.

---

### Machine Learning Model

Model Used:

Random Forest Classifier

Reasons for selection:

- Handles nonlinear behavioural relationships.
- Robust performance on simulated datasets.
- Reduced overfitting.
- Provides feature importance interpretation.

Outputs generated:

- Burnout Risk Classification.
- Dropout Probability Estimation.

---

## 🔎 Explainable AI — Behavioural Trigger Identification

To improve transparency and trust in AI predictions, SHAP (SHapley Additive exPlanations) is used.

SHAP enables:

- Understanding why a student is predicted high risk.
- Feature contribution visualization.
- Faculty decision support.

Example behavioural triggers identified:

- Low attendance percentage.
- High submission delays.
- Elevated dropout probability.

Explainability ensures actionable and interpretable outcomes.

---

## 🧩 Intervention Recommendation Engine

Intervention strategies are automatically generated based on predicted risk level.

Low Risk:

- Motivation reminders.
- Peer collaboration encouragement.

Medium Risk:

- Academic mentoring.
- Time management workshops.

High Risk:

- Counselling referrals.
- Faculty monitoring.
- Mental wellness programs.

The goal is preventive rather than reactive intervention.

---

## 📊 Dashboard Features

The visualization dashboard provides institutional analytics insights.

### Risk Score Gauge Meter

Displays overall university burnout risk index.

### Burnout Trend Analysis

Shows behavioural relationship between attendance and burnout risk.

### Dropout Probability Distribution

Identifies clusters of high-risk students.

### Student Risk Leaderboard

Ranks students based on burnout severity.

### Faculty Early Warning System

Automatically flags:

- High burnout risk students.
- Academic disengagement cases.

### Intervention Strategy Analytics

Displays frequency and effectiveness of recommended actions.

---

## 📁 Project Folder Structure

Student-Burnout-AI/

datasets/  
├── student_burnout_dataset.csv  
└── student_burnout_dataset_with_actions.csv  

notebooks/  
└── Student_Burnout_&_Dropout_Risk.ipynb  
  
README.md  

---

## 💻 Technology Stack

Programming Language:

Python

Libraries:

- Pandas
- NumPy
- Scikit-learn
- SHAP
- Plotly
- Seaborn
- Faker

Environment:

Google Colab

---

---

## 📈 Expected Outputs

The system produces:

- Burnout Risk Score (0–100).
- Burnout Risk Classification.
- Dropout Probability Prediction.
- Behavioural Trigger Explanation.
- Recommended Intervention Strategy.

Example Output:

StudentID: STU108

Risk Level: High

Behaviour Trigger:
Low Attendance + High Submission Delay

Recommended Intervention:
Counselling Support + Weekly Faculty Monitoring.

---

## 🔬 Ethical Considerations

- Dataset used is fully synthetic.
- No real student data collected.
- Intended strictly for academic and research experimentation.

---

## ✅ Results

The proposed system successfully detects behavioural burnout signals before academic failure occurs.

Key benefits:

- Early intervention opportunities.
- Faculty decision support.
- Institutional engagement monitoring.
- Reduced dropout probability.

---

## 🔮 Future Scope

- Integration with real LMS platforms.
- Real-time behavioural monitoring.
- NLP sentiment analysis from feedback text.
- Mobile faculty alert applications.
- Deep learning behavioural modelling.

---

## 🤝 Contribution

Pull requests are welcome.

Please open an issue before submitting major changes.

---

## 📜 License

Academic and Research Use Only.

---

## 👨‍💻 Author

**Etash Ashwin**
