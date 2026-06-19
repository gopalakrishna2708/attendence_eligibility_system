import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Attendance Eligibility System",
    layout="wide"
)

st.title(
    "Student Attendance Eligibility Prediction System"
)

df = pd.read_csv(
    "data/merged_attendance.csv"
)

model = pickle.load(
    open(
        "models/eligibility_model.pkl",
        "rb"
    )
)

st.subheader("Dataset")

st.dataframe(df)

st.subheader("Search Student")

student_email = st.text_input(
    "Enter Student Email"
)

if student_email:

    result = df[
        df["Email"].str.contains(
            student_email,
            case=False,
            na=False
        )
    ]

    st.dataframe(result)

st.subheader("Statistics")

eligible = len(
    df[df["Eligibility"]=="Eligible"]
)

not_eligible = len(
    df[df["Eligibility"]=="Not Eligible"]
)

col1,col2 = st.columns(2)

col1.metric(
    "Eligible Students",
    eligible
)

col2.metric(
    "Not Eligible Students",
    not_eligible
)

st.subheader("Download Results")

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download CSV",
    csv,
    file_name="attendance_results.csv",
    mime="text/csv"
)