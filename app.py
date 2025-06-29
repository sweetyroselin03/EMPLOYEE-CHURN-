import streamlit as st
import numpy as np

# --------------------- SETUP ---------------------
st.set_page_config(page_title="HR Login - Attrition Predictor", page_icon="🔐", layout="centered")

# --------------------- SESSION SETUP ---------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------------------- HR CREDENTIALS ---------------------
HR_USERNAME = "hr_admin"
HR_PASSWORD = "password123"  # You can improve this using keyring or encrypted auth

# --------------------- LOGIN PAGE ---------------------
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
            else:
                st.error("Invalid credentials. Try again.")

# --------------------- PREDICTION LOGIC ---------------------
def predict_attrition(projects, hours, time_spent, accident, promotion, salary):
    accident_val = 0 if accident == "No" else 1
    promotion_val = 0 if promotion == "No" else 1
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    # Dummy prediction
    if hours > 200 and projects <= 3 and promotion_val == 0 and salary_val == 0:
        return 1  # Will leave
    return 0  # Will stay

# --------------------- MAIN APP ---------------------
def attrition_app():
    st.title("💼 Employee Attrition Predictor")
    st.markdown("Welcome, HR! Use this tool to predict if an employee is likely to leave.")

    with st.form("attrition_form"):
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

    if submitted:
        result = predict_attrition(projects, hours, time_spent, accident, promotion, salary)
        st.markdown("---")
        if result == 1:
            st.error("🔴 The employee is likely to **leave**.")
        else:
            st.success("🟢 The employee is likely to **stay**.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# --------------------- PAGE ROUTING ---------------------
if not st.session_state.logged_in:
    login_page()
else:
    attrition_app()
