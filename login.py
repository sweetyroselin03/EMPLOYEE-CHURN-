import streamlit as st
from PIL import Image

# --- HR login credentials ---
HR_USERNAME = "hr_admin"
HR_PASSWORD = "password123"

# --- Page setup ---
st.set_page_config(page_title="HR Login", page_icon="🔐", layout="centered")

# --- Session state setup ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Page Function ---
def login_page():
    st.markdown("<h2 style='text-align: center;'>🔐 HR Login Portal</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)

    st.markdown("<p style='text-align:center; color: gray;'>Enter your credentials to access the HR tools</p>", unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        login_btn = st.form_submit_button("🔓 Login")

        if login_btn:
            if username == HR_USERNAME and password == HR_PASSWORD:
                st.session_state.logged_in = True
                st.experimental_set_query_params(page="dashboard")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")

# --- Routing to dashboard if already logged in ---
query = st.experimental_get_query_params()
if st.session_state.logged_in or query.get("page") == ["dashboard"]:
    st.switch_page("dashboard.py")
else:
    login_page()
