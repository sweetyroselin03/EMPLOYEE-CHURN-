import streamlit as st
import numpy as np
from PIL import Image

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="💼",
    layout="centered",
)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💼 Employee Attrition Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>A smart tool to predict whether an employee is likely to leave the company</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------- IMAGE / LOGO ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)

# ---------- INPUT FORM ----------
with st.form("prediction_form"):
    st.subheader("📊 Employee Information")

    col1, col2 = st.columns(2)
    with col1:
        projects = st.slider("Number of Projects", 1, 10, 3)
        time_spent = st.selectbox("Years at Company", list(range(1, 11)), index=2)
        promotion = st.radio("Promotion in Last 5 Years", ["No", "Yes"])
    with col2:
        hours = st.number_input("Average Monthly Hours", min_value=50, max_value=400, value=200)
        accident = st.radio("Work Accident", ["No", "Yes"])
        salary = st.selectbox("Salary Level", ["Low", "Medium", "High"])

    submitted = st.form_submit_button("🔍 Predict")

# ---------- PREDICTION LOGIC ----------
def predict_attrition(projects, hours, time_spent, accident, promotion, salary):
    accident_val = 0 if accident == "No" else 1
    promotion_val = 0 if promotion == "No" else 1
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    # Simulated prediction logic (replace with real model)
    if hours > 200 and projects <= 3 and promotion_val == 0 and salary_val == 0:
        return 1  # Will leave
    return 0  # Will stay

# ---------- SHOW RESULT ----------
if submitted:
    result = predict_attrition(projects, hours, time_spent, accident, promotion, salary)

    st.markdown("---")
    if result == 1:
        st.error("🔴 The employee is likely to **leave** the organization.")
    else:
        st.success("🟢 The employee is likely to **stay** with the organization.")

# ---------- FOOTER ----------
st.markdown("""---  
<p style='text-align: center; font-size: 14px; color: gray'>
Made with ❤️ by Your Name | © 2025
</p>""", unsafe_allow_html=True)
