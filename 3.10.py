import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'dept_id': [101, 102, 103]
})

departments = pd.DataFrame({
    'dept_id': [101, 102, 104],
    'dept_name': ['HR', 'Engineering', 'Marketing']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 4],
    'salary': [5000, 6000, 7000]
})

print("One-to-one merge:")
print(pd.merge(employees, salaries, on='emp_id'))

projects = pd.DataFrame({
    'dept_id': [101, 101, 102, 103],
    'project': ['P1', 'P2', 'P3', 'P4']
})

print("\nMany-to-one merge:")
print(pd.merge(employees, departments, on='dept_id'))

print("\nMany-to-many merge:")
print(pd.merge(employees, projects, on='dept_id'))

employees2 = pd.DataFrame({
    'employee_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

print("\nMerge with different column names:")
print(pd.merge(employees2, salaries, left_on='employee_id', right_on='emp_id'))

employees_idx = employees.set_index('emp_id')
salaries_idx = salaries.set_index('emp_id')

print("\nJoin on index:")
print(employees_idx.join(salaries_idx, how='left'))

print("\nMerge three DataFrames:")
merged = pd.merge(
    pd.merge(employees, salaries, on='emp_id', how='outer', indicator=True),
    departments,
    on='dept_id',
    how='left'
)
print(merged)