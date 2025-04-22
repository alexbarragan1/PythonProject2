import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [88, 92, 79, 93],
    'Department': ['HR', 'Tech', 'Tech', 'HR']
}
df = pd.DataFrame(data)

print("Using .loc:")
print(df.loc[1:2, ['Name', 'Score']])

print("\nUsing .iloc:")
print(df.iloc[1:3, [0, 2]])

print("\nEmployees in Tech department:")
print(df[df['Department'] == 'Tech'])

print("\nScores above 90:")
print(df[df['Score'] > 90])

df.loc[df['Age'] > 30, 'Score'] = 95
print("\nAfter updating scores:")
print(df)

df = df.set_index('Name')
print("\nDataFrame with Name as index:")
print(df)

print("\nSlicing with .loc:")
print(df.loc['Bob':'Diana', ['Age', 'Score']])

print("\nSlicing with .iloc:")
print(df.iloc[1:3, 0:2])