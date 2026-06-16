import streamlit as st
from services.auth.login import display_login

def main():
    st.set_page_config(
        page_icon="🏋️",
        page_title="AI GYM COACH",
        initial_sidebar_state="expanded",
        layout="centered"
    )
    
    if not display_login():
        return
    st.write('hello')
    
if __name__ == "__main__":
    main()