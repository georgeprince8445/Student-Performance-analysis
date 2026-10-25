"""
Student Performance Analytics System
Reads student records from students.csv, calculates results, and prints analytics.
"""

from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "students.csv"
PASSING_MARKS_PER_SUBJECT = 35  # A student must score at least 35 in every subject to pass.


def assign_grade(average: float) -> str:
    """Return a letter grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    if average >= 35:
        return "E"
    return "F"


def analyze_students(data_file: Path = DATA_FILE) -> None:
    """Load the CSV, calculate student results, and display class analytics."""
    if not data_file.exists():
        raise FileNotFoundError(
            f"Dataset not found: {data_file}\n"
            "Keep students.csv in the same folder as main.py."
        )

    df = pd.read_csv(data_file)
    required_columns = [
        "Student_ID", "Name", "Department", "Marks_Math",
        "Marks_Science", "Marks_English", "Attendance"
    ]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in students.csv: {missing}")
    if df.empty:
        raise ValueError("students.csv contains no student records.")

    subject_columns = ["Marks_Math", "Marks_Science", "Marks_English"]

    # NumPy/Pandas calculations
    df["Total_Marks"] = df[subject_columns].sum(axis=1)
    df["Average_Marks"] = df[subject_columns].mean(axis=1).round(2)
    df["Grade"] = df["Average_Marks"].apply(assign_grade)
    df["Status"] = np.where(
        (df[subject_columns] >= PASSING_MARKS_PER_SUBJECT).all(axis=1),
        "Pass",
        "Fail"
    )

    # Friendly column labels for the printed report
    display_df = df.rename(columns={
        "Student_ID": "Student ID",
        "Marks_Math": "Math",
        "Marks_Science": "Science",
        "Marks_English": "English",
        "Total_Marks": "Total",
        "Average_Marks": "Average",
    })

    print("\n" + "=" * 104)
    print("                 STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 104)
    print(display_df[
        ["Student ID", "Name", "Department", "Math", "Science", "English",
         "Total", "Average", "Grade", "Status", "Attendance"]
    ].to_string(index=False))

    all_marks = df[subject_columns].to_numpy()
    print("\n" + "-" * 104)
    print("CLASS PERFORMANCE ANALYTICS")
    print("-" * 104)
    print(f"Number of students       : {len(df)}")
    print(f"Highest individual mark  : {np.max(all_marks)}")
    print(f"Lowest individual mark   : {np.min(all_marks)}")
    print(f"Overall class average    : {df['Average_Marks'].mean():.2f}")
    print(f"Class pass rate          : {(df['Status'].eq('Pass').mean() * 100):.2f}%")
    print(f"Average attendance       : {df['Attendance'].mean():.2f}%")
    print(f"Highest student average  : {df['Average_Marks'].max():.2f}")
    print(f"Lowest student average   : {df['Average_Marks'].min():.2f}")

    subject_averages = df[subject_columns].mean().round(2)
    print("\nSubject-wise averages:")
    for subject, average in subject_averages.items():
        print(f"  {subject.replace('Marks_', ''):<10}: {average:.2f}")

    print("\nGrade distribution:")
    grade_order = ["A+", "A", "B", "C", "D", "E", "F"]
    grade_counts = df["Grade"].value_counts()
    for grade in grade_order:
        print(f"  {grade:<3}: {int(grade_counts.get(grade, 0))}")

    print("\nNote: Pass requires at least 35 marks in every subject.")


if __name__ == "__main__":
    analyze_students()
