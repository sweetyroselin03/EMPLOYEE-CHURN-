# app.py

import streamlit as st
import numpy as np

# Simulated Machine Learning Model
def predict_employee_attrition(projects, hours, time_spent, accident, promotion, salary):
    # Encode categorical variables
    accident_val = 0 if accident == "No" else 1
    promotion_val = 0 if promotion == "No" else 1
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    # Example logic to simulate model prediction
    # Replace with: prediction = model.predict([[...]])
    if (
        projects <= 3
        and hours > 200
        and time_spent >= 3
        and accident_val == 0
        and promotion_val == 0
        and salary_val == 0
    ):
        return 1  # Will leave
    else:
        return 0  # Will stay

# Streamlit App UI
st.set_page_config(page_title="Employee Attrition Predictor", layout="centered")
st.title("Employee Attrition Predictor (HR Analytics)")

st.markdown("### Input Employee Details:")

# Inputs
projects = st.number_input("Number of Projects", min_value=1, max_value=10, value=3)
hours = st.number_input("Average Monthly Hours", min_value=50, max_value=400, value=201)
time_spent = st.number_input("Time Spent at Company (Years)", min_value=0, max_value=20, value=3)

accident = st.selectbox("Work Accident", ["No", "Yes"])
promotion = st.selectbox("Promotion in Last 5 Years", ["No", "Yes"])
salary = st.selectbox("Salary", ["Low", "Medium", "High"])

# Prediction
if st.button("Predict"):
    result = predict_employee_attrition(projects, hours, time_spent, accident, promotion, salary)
    st.markdown("---")
    if result == 1:
        st.error("🔴 The employee is predicted to leave.")
    else:
        st.success("🟢 The employee is predicted to stay.")

