import streamlit as st
import numpy as np

# ----------------- SETUP -----------------
st.set_page_config(page_title="HR Login - Attrition Predictor", page_icon="🔐", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- HR CREDENTIALS -----------------
HR_USERNAME = "hr_admin"
HR_PASSWORD = "password123"

# ----------------- LOGIN PAGE -----------------
def login_page():
    st.title("🔐 HR Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if username == HR_USERNAME and password == HR_PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful. Welcome HR!")
                st.rerun()
            else:
                st.error("Invalid credentials. Try again.")

# ----------------- PREDICTION LOGIC -----------------
def predict_attrition(data):
    """
    Dummy logic for demonstration:
    If job satisfaction or environment satisfaction is very low,
    and average monthly hours are high, assume high risk of attrition.
    """
    if data['JobSatisfaction'] <= 2 and data['EnvironmentSatisfaction'] <= 2:
        if data['Average_Monthly_Hours'] > 220 or data['Salary'] == "Low":
            return 1  # Likely to leave
    return 0  # Likely to stay

# ----------------- MAIN APP -----------------
def attrition_app():
    st.title("💼 Employee Attrition Predictor")
    st.markdown("Welcome, HR! Use this tool to predict if an employee is likely to leave.")

    with st.form("attrition_form"):
        st.subheader("📋 Employee Information")

        col1, col2 = st.columns(2)
        with col1:
            projects = st.slider("Number of Projects", 1, 10, 3)
            hours = st.number_input("Average Monthly Hours", min_value=50, max_value=400, value=200)
            time_spent = st.selectbox("Years at Company", list(range(1, 11)), index=2)
            accident = st.radio("Work Accident", ["No", "Yes"])
            promotion = st.radio("Promotion in Last 5 Years", ["No", "Yes"])
        with col2:
            salary = st.selectbox("Salary Level", ["Low", "Medium", "High"])
            department = st.selectbox("Department", [
                "Sales", "Technical", "Support", "IT", "HR", "Accounting", "Marketing", "R&D", "Management"
            ])
            job_sat = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
            env_sat = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        data = {
            'Number_of_Projects': projects,
            'Average_Monthly_Hours': hours,
            'Time_Spent_at_Company': time_spent,
            'Work_Accident': accident,
            'Promotion_in_Last_5_Years': promotion,
            'Salary': salary,
            'Department': department,
            'JobSatisfaction': job_sat,
            'EnvironmentSatisfaction': env_sat
        }

        result = predict_attrition(data)
        st.markdown("---")
        if result == 1:
            st.error("🔴 The employee is likely to **leave**.")
        else:
            st.success("🟢 The employee is likely to **stay**.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ----------------- PAGE ROUTING -----------------
if not st.session_state.logged_in:
    login_page()
else:
    attrition_app()
