# Student Performance Analytics System

## 1. Project Overview
The **Student Performance Analytics System** is a beginner-friendly Python project that reads student records from a CSV file, calculates marks and grades, checks pass/fail status, and summarizes class performance.

## 2. Objectives
- Store student details and marks in a structured CSV dataset.
- Calculate each student's total and average marks.
- Assign a grade based on average marks.
- Identify whether each student passes or fails.
- Calculate the highest and lowest individual marks, overall class average, and subject-wise averages.
- Present the results in a clean terminal report.

## 3. Technologies Used
- **Python 3** — program logic
- **Pandas** — CSV reading, tabular processing, and summary calculations
- **NumPy** — numeric calculations and pass/fail status
- **CSV** — dataset storage

## 4. Project Structure
```text
Student_Performance_Analytics_System/
├── main.py
├── students.csv
└── README.md
```

## 5. Dataset Description
`students.csv` contains 15 sample student records with these columns:

| Column | Description |
|---|---|
| `Student_ID` | Unique student identifier |
| `Name` | Student name |
| `Department` | Student's department |
| `Marks_Math` | Mathematics marks out of 100 |
| `Marks_Science` | Science marks out of 100 |
| `Marks_English` | English marks out of 100 |
| `Attendance` | Attendance percentage |

The dataset contains fictional sample data for demonstration.

## 6. Grade and Pass/Fail Rules
### Grade based on average marks
| Average | Grade |
|---:|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 35–49.99 | E |
| Below 35 | F |

### Pass/Fail
A student passes only if they score **at least 35 marks in each of the three subjects**. If any subject score is below 35, the student fails.

## 7. Implementation Steps
1. Install Python 3 if it is not already installed.
2. Open a terminal in the project folder.
3. Install dependencies:
   ```bash
   python -m pip install pandas numpy
   ```
4. Run the script:
   ```bash
   python main.py
   ```
5. Read the student result table and class analytics displayed in the terminal.

## 8. Calculations Performed
- **Total Marks:** sum of Math, Science, and English marks.
- **Average Marks:** total marks divided by 3.
- **Highest/Lowest Individual Mark:** maximum/minimum among all marks in the three subjects.
- **Overall Class Average:** mean of the students' average marks.
- **Subject-wise Average:** mean mark for each subject.
- **Pass Rate:** percentage of students marked Pass.

## 9. Final Outcome
When `main.py` runs successfully, it displays each student's total, average, grade, and status, followed by class-level statistics, subject averages, grade distribution, pass rate, and average attendance.

## 10. Possible Improvements
- Load records from a database.
- Add charts for subject and department comparisons.
- Export the processed results to a new CSV or Excel file.
- Add input validation for marks and attendance ranges.
