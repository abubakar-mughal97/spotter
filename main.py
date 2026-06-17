import streamlit as st
from services.auth.login import display_login
from services.state.session_defaults import initital_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS


def main():
    st.set_page_config(
        page_icon="🏋️",
        page_title="Spotter",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    if not display_login():
        return
    initital_session_defaults()

    workout_started = st.session_state.get("workout_started")

    with st.sidebar:
        st.title("🏋️ Spotter - Your Personal AI Coach")

        if st.session_state.get("username"):
            st.caption(f"Welcome, **{st.session_state['username']}**!")
        st.divider()

        st.subheader("Workout Plan")
        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")
            st.number_input("Sets", min_value=0, max_value=20, key="plan_sets", step=1)
            st.number_input("Reps", min_value=0, max_value=100, key="plan_reps", step=1)
            st.markdown("Click the button below to start your workout session.")
            start_session_button = st.button(
                "Start Session", width="stretch", key="start_session_button"
            )

            if start_session_button:
                st.session_state["workout_started"] = True
                st.rerun()
        else:
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")
            print(exercise, sets, reps)

            st.info(f"****{exercise} - {sets} sets of {reps} reps****")

            end_session_button = st.button(
                "End Session", width="stretch", key="end_session_button"
            )
            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()

        if workout_started:
            st.divider()

            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")

            st.subheader("Progress")

            st.metric("Total Reps", total_reps)
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.get('knee_angle')}°")
                st.metric("Back Angle", f"{st.session_state.get('back_angle')}°")
                st.metric("Depth Status", st.session_state.get("depth_status"))
            elif exercise == "Push-ups":
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Body Alignment", st.session_state.get("body_alignment"))
                st.metric("Hip Position", st.session_state.get("hip_status"))
            elif exercise == "Bicep Curls (Dumbbells)":
                st.subheader("Bicep Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Shoulder Status", st.session_state.get("shoulder_status"))
                st.metric("Swing Status", st.session_state.get("swing_status"))
            elif exercise == "Shoulder Press (Dumbbells)":
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Arm Extension", st.session_state.get("extension_status"))
                st.metric("Back Arch", st.session_state.get("back_arch_status"))
            elif exercise == "Lunges":
                st.subheader("Lunge Metrics")
                st.metric(
                    "Front Knee Angle", f"{st.session_state.get('front_knee_angle')}°"
                )
                st.metric("Torso Angle", f"{st.session_state.get('torse_angle')}°")
                st.metric("Balance Status", st.session_state.get("balance_status"))


if __name__ == "__main__":
    main()
