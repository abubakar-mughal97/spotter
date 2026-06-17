import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def display_login() -> bool:
    if st.session_state.get("username") is not None:
        return True

    st.title("🏋️ Spotter - Your Personal AI Coach")
    st.markdown(
        "Welcome to Spotter. Your personal AI Coach. Please enter a username to start"
    )

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name", placeholder="Enter a name")
        submitted = st.form_submit_button("Start Session")

    if submitted and username.strip():
        user = get_or_create_user(username)
        st.session_state["username"] = user["username"]
        st.session_state["user_id"] = user["id"]

        return True
    else:
        st.error("Name cannot be empty.")
        return False
