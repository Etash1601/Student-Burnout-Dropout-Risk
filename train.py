import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

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

df = pd.read_csv("student_burnout_dataset_with_actions.csv")

df["Risk_Label"] = df["Burnout_Risk_Level"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

X = df[FEATURES]
y = df["Risk_Label"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

pickle.dump(model, open("burnout_model.pkl", "wb"))

print("Model saved successfully")