import pandas as pd
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'GPA': [3.8, 3.5, 4.0],
    'On_Campus': [True, False, True],
    'Graduation_Date': pd.to_datetime(['2024-05-15', '2023-12-20', '2025-05-20'])
}

students = pd.DataFrame(student_data)
print("\nStudent DataFrame:")
print(students)

print("\nData types:")
print(students.dtypes)

print("\nSummary statistics:")
print(students.describe(include='all'))