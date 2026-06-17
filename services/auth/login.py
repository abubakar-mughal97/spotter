import streamlit as st
from services.persistence.exercise_repository import register_user, verify_user


def display_login() -> bool:
    if st.session_state.get("username") is not None:
        return True

    st.title("🏋️ Spotter - Your Personal AI Coach")
    st.markdown(
        "Welcome to Spotter. Your personal AI Coach. Please enter a username to start"
    )

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input(
        "Password", placeholder="Enter your password", type="password"
    )

    (
        col1,
        col2,
    ) = st.columns(2)
    with col1:
        login_clicked = st.button("Start Session", width="stretch")

    with col2:
        register_clicked = st.button("Register", width="stretch")

    if login_clicked:
        if not username.strip() or not password:
            st.error("Please enter both a username and password.")
            return False
        user = verify_user(username, password)
        if user is None:
            st.error("Invalid username or password.")
            return False

        st.session_state["username"] = user["username"]
        st.session_state["user_id"] = user["id"]
        st.rerun()

    if register_clicked:
        if not username.strip() or not password:
            st.error("Please enter both a username and a password.")
            return False

        user = register_user(username, password)
        if user is None:
            st.error("That username is already taken. Try logging in instead.")
            return False

        st.session_state["username"] = user["username"]
        st.session_state["user_id"] = user["id"]
        st.rerun()

        return False
