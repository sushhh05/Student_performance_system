import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("student_model.pkl")

st.title("🎓 Student Performance Prediction App")

st.write("Enter student details to predict overall score")

# ---- User Inputs ----
study_hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0)
attendance_percentage = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)

school_type = st.selectbox("School Type", ["public", "private"])
school_type_encoded = 1 if school_type == "public" else 0

internet_access = st.selectbox("Internet Access", ["yes", "no"])
internet_access_encoded = 1 if internet_access == "yes" else 0

extra_activities = st.selectbox("Extra Activities", ["yes", "no"])
extra_activities_encoded = 1 if extra_activities == "yes" else 0

study_method = st.selectbox(
    "Study Method",
    ["coaching", "group_study", "mixed", "notes", "online_videos", "textbook"]
)

study_method_coaching = 1 if study_method == "coaching" else 0
study_method_group_study = 1 if study_method == "group_study" else 0
study_method_mixed = 1 if study_method == "mixed" else 0
study_method_notes = 1 if study_method == "notes" else 0
study_method_online_videos = 1 if study_method == "online_videos" else 0
study_method_textbook = 1 if study_method == "textbook" else 0

# ---- Prediction Button ----
if st.button("Predict Overall Score"):
    prediction = model.predict([[
        study_hours,
        attendance_percentage,
        school_type_encoded,
        internet_access_encoded,
        extra_activities_encoded,
        study_method_coaching,
        study_method_group_study,
        study_method_mixed,
        study_method_notes,
        study_method_online_videos,
        study_method_textbook
    ]])

    st.success(f"📊 Predicted Overall Score: {round(prediction[0], 2)}")   
    
    #prediction[0] here [0] is written because prediction outout comes in array
    #so it takes the 0th index value to display..and we cant directly use round function on array.
