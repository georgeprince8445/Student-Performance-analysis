import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analytics Dashboard")
st.write("Explore student marks, averages, grades, and pass/fail performance.")

# Load the CSV from the same folder as this script.
csv_path = Path(__file__).parent / "students.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

try:
    df = load_data(csv_path)
except Exception:
    # Fallback data ensures the app still displays a working dashboard
    # if students.csv was not uploaded to the repository.
    df = pd.DataFrame({
        "Student_ID": [1, 2, 3, 4, 5, 6],
        "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sara"],
        "Math": [85, 72, 91, 58, 66, 95],
        "Science": [88, 79, 93, 62, 70, 96],
        "English": [81, 84, 89, 65, 74, 92],
    })
    st.info("Using demo data because students.csv was not found. Upload students.csv to use your full dataset.")

# Standardize common column names and identify numeric score columns.
name_col = next((c for c in df.columns if c.lower() in ["name", "student_name", "student"]), None)
id_col = next((c for c in df.columns if c.lower() in ["student_id", "id", "roll_no", "roll_number"]), None)
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
score_cols = [c for c in numeric_cols if c != id_col]

if not score_cols:
    st.error("No numeric score columns were found in the dataset. Add numeric subject-mark columns to students.csv.")
    st.dataframe(df, use_container_width=True)
    st.stop()

df["Average"] = df[score_cols].mean(axis=1).round(2)
df["Total"] = df[score_cols].sum(axis=1).round(2)

def grade(avg):
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"

df["Grade"] = df["Average"].apply(grade)
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", len(df))
c2.metric("Class Average", f"{df['Average'].mean():.1f}%")
c3.metric("Highest Average", f"{df['Average'].max():.1f}%")
c4.metric("Pass Rate", f"{(df['Result'].eq('Pass').mean() * 100):.1f}%")

st.subheader("📋 Student Results")
search = st.text_input("Search student name or ID", "")
view = df.copy()
if search:
    searchable = view.astype(str).apply(lambda col: col.str.contains(search, case=False, na=False)).any(axis=1)
    view = view[searchable]
st.dataframe(view, use_container_width=True, hide_index=True)

left, right = st.columns(2)
with left:
    st.subheader("Average Score by Student")
    chart_label = name_col if name_col else (id_col if id_col else df.columns[0])
    chart_data = df.set_index(chart_label)["Average"]
    st.bar_chart(chart_data)
with right:
    st.subheader("Grade Distribution")
    grade_counts = df["Grade"].value_counts().sort_index()
    st.bar_chart(grade_counts)

st.subheader("📚 Subject Averages")
subject_averages = df[score_cols].mean().round(2).sort_values(ascending=False)
st.bar_chart(subject_averages)

st.caption("Demo dashboard built with Streamlit, Pandas, and NumPy.")
