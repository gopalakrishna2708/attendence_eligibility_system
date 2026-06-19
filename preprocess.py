import pandas as pd

# Load datasets
day1 = pd.read_csv("data/day1.csv")
day2 = pd.read_csv("data/day2.csv")

# Use Email column as unique identifier
day1_students = set(day1['Email'])
day2_students = set(day2['Email'])

all_students = list(day1_students.union(day2_students))

attendance_data = []

for student in all_students:

    d1 = "P" if student in day1_students else "A"
    d2 = "P" if student in day2_students else "A"

    present_days = [d1, d2].count("P")
    total_days = 2

    attendance_percentage = (
        present_days / total_days
    ) * 100

    eligibility = (
        "Eligible"
        if attendance_percentage >= 80
        else "Not Eligible"
    )

    attendance_data.append([
        student,
        d1,
        d2,
        present_days,
        total_days,
        attendance_percentage,
        eligibility
    ])

merged = pd.DataFrame(
    attendance_data,
    columns=[
        "Email",
        "Day1",
        "Day2",
        "Present_Days",
        "Total_Days",
        "Attendance_Percentage",
        "Eligibility"
    ]
)

merged.to_csv(
    "data/merged_attendance.csv",
    index=False
)

print("Merged dataset created.")