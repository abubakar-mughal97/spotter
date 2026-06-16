import streamlit as st

def display_login() -> bool:
    if st.session_state.get("username") is not None:
        return True

    st.title("AI GYM COACH")
    st.markdown("Welcome to your personal AI Coach. Please enter a username to start")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name", placeholder="Enter a name")
        submitted = st.form_submit_button("Start Session")

    if submitted and username.strip():
        st.session_state["username"] = username.strip()
        return True
    else:
        st.error("Name cannot be empty.")
        return False
