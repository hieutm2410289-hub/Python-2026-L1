import pandas as pd

students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')

print(students.isnull().sum())
print(scores.isnull().sum())

students = students.dropna(subset=['student_id', 'name', 'major'])

score_cols = ['python', 'math', 'database']
for col in score_cols:
    scores[col] = scores[col].fillna(scores[col].mean())

scores['average_score'] = scores[score_cols].mean(axis=1)

merged_df = pd.merge(students, scores, on='student_id', how='inner')

student_avg = merged_df[['student_id', 'name', 'major', 'average_score']]
print(student_avg)

top_5 = student_avg.sort_values(by='average_score', ascending=False).head(5)
print(top_5)

major_avg = merged_df.groupby('major')['average_score'].mean().reset_index()
print(major_avg)