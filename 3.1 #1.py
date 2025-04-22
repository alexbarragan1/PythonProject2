import pandas as pd
scores = pd.Series([88, 92, 79, 93, 85],
                  index=['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
                  name='Exam Scores')
print("Exam Scores:")
print(scores)

top_scorer = scores.idxmax()
top_score = scores.max()

print(f"\nTop scorer: {top_scorer} with {top_score} points")

average = scores.mean()
above_avg = scores[scores > average]

print("\nStudents scoring above average:")
print(above_avg)