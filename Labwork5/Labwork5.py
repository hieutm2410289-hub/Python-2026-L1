import pandas as pd

# ==========================================
# PHẦN 1: TẢI VÀ XỬ LÝ DỮ LIỆU KHUYẾT
# ==========================================

students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')

print(students.isnull().sum())
print(scores.isnull().sum())

students = students.dropna(subset=['student_id', 'name', 'major'])

subject_cols = ['python', 'math', 'database']
for col in subject_cols:
    scores[col] = scores[col].fillna(scores[col].mean())

scores['score'] = scores[subject_cols].mean(axis=1)

merged_df = pd.merge(students, scores, on='student_id', how='inner')


# ==========================================
# PHẦN 2: THỐNG KÊ VÀ XUẤT KẾT QUẢ
# ==========================================

student_avg = merged_df.groupby(['student_id', 'name', 'major'])['score'].mean().reset_index()
student_avg.rename(columns={'score': 'average_score'}, inplace=True)

print(student_avg)

top_5 = student_avg.sort_values(by='average_score', ascending=False).head(5)

print(top_5)

major_avg = merged_df.groupby('major')['score'].mean().reset_index()
major_avg.rename(columns={'score': 'average_score'}, inplace=True)

print(major_avg)