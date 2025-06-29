import streamlit as st
from PIL import Image
import numpy as np

# --- Set up the page ---
st.set_page_config(page_title="HR Portal - Attrition Predictor", page_icon="🧠", layout="centered")

# --- HR login credentials ---
HR_USERNAME = "hr_admin"
HR_PASSWORD = "password123"

# --- Initialize session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Page ---
def login_page():
    st.markdown("<h2 style='text-align: center;'>🔐 HR Login Portal</h2>", unsafe_allow_html=True)

    # Centered logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)

    st.markdown("<p style='text-align:center; color: gray;'>Enter your credentials to access the HR tools</p>", unsafe_allow_html=True)

    # Login form
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        login_btn = st.form_submit_button("🔓 Login")

        if login_btn:
            if username == HR_USERNAME and password == HR_PASSWORD:
                st.session_state.logged_in = True
                st.success("✅ Login successful!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")

# --- Prediction Function ---
def predict_attrition(projects, hours, time_spent, accident, promotion, salary):
    accident_val = 0 if accident == "No" else 1
    promotion_val = 0 if promotion == "No" else 1
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    # Simple logic for demo purposes
    if hours > 200 and projects <= 3 and promotion_val == 0 and salary_val == 0:
        return 1
    return 0

# --- Dashboard Page ---
def dashboard():
    st.markdown("<h2 style='text-align: center;'>👩‍💼 HR Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("Use this form to predict employee attrition:")

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

    # Logout
    if st.button("🔒 Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# --- Routing Logic ---
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
