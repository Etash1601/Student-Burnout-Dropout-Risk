import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle

# =============================
# Config
# =============================

st.set_page_config(
    page_title="Student Burnout Risk System",
    layout="wide"
)

FEATURES = [
    "LMS_Logins_Per_Week",
    "Login_Drop_Ratio",
    "Attendance_Percentage",
    "Attendance_Trend",
    "Avg_Assignment_Delay_Days",
    "Late_Submission_Ratio",
    "Night_Activity_Ratio",
    "Avg_Session_Duration_Min",
    "Sentiment_Score"
]

risk_map = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk"
}

# =============================
# Load model
# =============================

@st.cache_resource
def load_model():
    return pickle.load(open("burnout_model.pkl", "rb"))

model = load_model()

# =============================
# Load dataset
# =============================

@st.cache_data
def load_data():
    return pd.read_csv("student_burnout_dataset_with_actions.csv")

df = load_data()

# =============================
# Title
# =============================

st.title("🎓 Student Burnout Risk Prediction System")

# =============================
# Dashboard Section
# =============================

st.header("📊 Dashboard")

col1, col2 = st.columns(2)

# Gauge chart
avg_risk = df["Burnout_Risk_Score"].mean()

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=avg_risk,
    title={'text': "Average Burnout Risk"},
    gauge={
        'axis': {'range': [0,100]},
        'steps': [
            {'range': [0,33], 'color': "green"},
            {'range': [33,66], 'color': "yellow"},
            {'range': [66,100], 'color': "red"}
        ]
    }
))

col1.plotly_chart(fig, use_container_width=True)

# Pie chart
fig2 = px.pie(
    df,
    names="Burnout_Risk_Level",
    title="Risk Level Distribution"
)

col2.plotly_chart(fig2, use_container_width=True)

# Histogram
st.subheader("Burnout Risk Distribution")

fig3 = px.histogram(
    df,
    x="Burnout_Risk_Score",
    nbins=30,
    color="Burnout_Risk_Level"
)

st.plotly_chart(fig3, use_container_width=True)

# Feature importance
st.subheader("Feature Importance")

importance = model.feature_importances_

imp_df = pd.DataFrame({
    "Feature": FEATURES,
    "Importance": importance
}).sort_values("Importance")

fig4 = px.bar(
    imp_df,
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(fig4, use_container_width=True)

# =============================
# Prediction Section
# =============================

st.header("🔮 Predict New Student Risk")

col1, col2, col3 = st.columns(3)

with col1:
    lms = st.number_input("LMS Logins", 0.0, 20.0, 5.0)
    login_drop = st.slider("Login Drop Ratio", 0.0, 1.0, 0.2)
    attendance = st.slider("Attendance %", 0.0, 100.0, 75.0)

with col2:
    trend = st.slider("Attendance Trend", -50.0, 50.0, -5.0)
    delay = st.slider("Assignment Delay", 0.0, 20.0, 2.0)
    late = st.slider("Late Submission Ratio", 0.0, 1.0, 0.3)

with col3:
    night = st.slider("Night Activity Ratio", 0.0, 1.0, 0.3)
    session = st.slider("Session Duration", 5.0, 200.0, 40.0)
    sentiment = st.slider("Sentiment Score", -1.0, 1.0, 0.0)

if st.button("Predict Risk"):

    input_df = pd.DataFrame({

        "LMS_Logins_Per_Week": [lms],
        "Login_Drop_Ratio": [login_drop],
        "Attendance_Percentage": [attendance],
        "Attendance_Trend": [trend],
        "Avg_Assignment_Delay_Days": [delay],
        "Late_Submission_Ratio": [late],
        "Night_Activity_Ratio": [night],
        "Avg_Session_Duration_Min": [session],
        "Sentiment_Score": [sentiment]

    })

    prediction = model.predict(input_df)[0]

    risk = risk_map[prediction]

    st.success(f"Predicted Risk Level: {risk}")

    # Prediction gauge
    fig_pred = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction * 50,
        title={'text': "Prediction Level"},
        gauge={
            'axis': {'range': [0,100]},
            'steps': [
                {'range': [0,33], 'color': "green"},
                {'range': [33,66], 'color': "yellow"},
                {'range': [66,100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(fig_pred, use_container_width=True)