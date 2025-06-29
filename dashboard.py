import streamlit as st
import numpy as np

st.set_page_config(page_title="HR Dashboard", page_icon="👩‍💼", layout="centered")

# --- Check login ---
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ You must log in first.")
    st.switch_page("login.py")

# --- Main Dashboard ---
st.markdown("<h2 style='text-align: center;'>👩‍💼 HR Dashboard</h2>", unsafe_allow_html=True)
st.success("🎉 You have access to the secure HR tools.")

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

def predict_attrition(projects, hours, time_spent, accident, promotion, salary):
    accident_val = 0 if accident == "No" else 1
    promotion_val = 0 if promotion == "No" else 1
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    if hours > 200 and projects <= 3 and promotion_val == 0 and salary_val == 0:
        return 1
    return 0

if submitted:
    result = predict_attrition(projects, hours, time_spent, accident, promotion, salary)
    st.markdown("---")
    if result == 1:
        st.error("🔴 The employee is likely to **leave**.")
    else:
        st.success("🟢 The employee is likely to **stay**.")

# --- Logout Button ---
if st.button("🔒 Logout"):
    st.session_state.logged_in = False
    st.experimental_set_query_params()
    st.switch_page("login.py")
