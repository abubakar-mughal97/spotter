import streamlit as st


def initital_session_defaults():
    defaults = {
        "reps": 0,
        "target_sets": 0,
        "sets_completed": 0,
        "current_set_reps": 0,
        "workout_complete": False,
        "last_notified_sets_completed": 0,
        "last_notifies_workout_complete": 0,
        "last_saved_sets_complete": 0,
        "set_cycle_started_at": 0.0,
        "last_exercise_type": "Squats",
        # Workout
        "workout_started": False,
        "plan_exercise": "Squats",
        "plan_sets": 3,
        "plan_reps": 10,
        # Angles
        "knee_angle": 0,
        "back_angle": 0,
        "elbow_angle": 0,
        "front_knee_angle": 0,
        "torse_angle": 0,
        # Status
        "depth_status": "N/A",
        "body_alignment": "N/A",
        "hip_status": "N/A",
        "shoulder_status": "N/A",
        "swing_status": "N/A",
        "extension_status": "N/A",
        "back_arch_status": "N/A",
        "balance_status": "N/A",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
