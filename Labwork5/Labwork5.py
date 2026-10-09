import pandas as pd

# ==============================================================================
# PART 1: DATA MANIPULATION (students.csv)
# ==============================================================================
print("=" * 60)
print("PART 1: DATA MANIPULATION")
print("=" * 60)

# Load the dataset
students_df = pd.read_csv('students.csv')

# Display first five rows
print("\n--- First 5 rows ---")
print(students_df.head())

# Find number of rows and columns
rows, cols = students_df.shape
print(f"\nNumber of rows: {rows}, Number of columns: {cols}")

# Select name and GPA
if 'name' in students_df.columns and 'GPA' in students_df.columns:
    name_gpa = students_df[['name', 'GPA']]
    print("\n--- Name and GPA ---")
    print(name_gpa.head())

# Find students with GPA >= 3.5
if 'GPA' in students_df.columns:
    high_gpa_students = students_df[students_df['GPA'] >= 3.5]
    print("\n--- Students with GPA >= 3.5 ---")
    print(high_gpa_students)

# Sort students by GPA
if 'GPA' in students_df.columns:
    sorted_students = students_df.sort_values(by='GPA', ascending=False)
    print("\n--- Students sorted by GPA (Descending) ---")
    print(sorted_students.head())

# Find average GPA by major
if 'major' in students_df.columns and 'GPA' in students_df.columns:
    avg_gpa_by_major = students_df.groupby('major')['GPA'].mean().round(2).reset_index()
    print("\n--- Average GPA by Major ---")
    print(avg_gpa_by_major)


# ==============================================================================
# PART 2: FROM RAW DATA TO USEFUL INFO (students.csv & scores.csv)
# ==============================================================================
print("\n" + "=" * 60)
print("PART 2: FROM RAW DATA TO USEFUL INFO")
print("=" * 60)

# Load both files
students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')

# Check missing values
print("\n--- Missing values in students.csv ---")
print(students.isnull().sum())

print("\n--- Missing values in scores.csv ---")
print(scores.isnull().sum())

# Clean ID columns
students = students.dropna(subset=['student_id'])
scores = scores.dropna(subset=['student_id'])

# Auto-detect the score column (find numerical columns in scores.csv except student_id)
numeric_cols = scores.select_dtypes(include=['number']).columns.tolist()
score_col = [col for col in numeric_cols if col != 'student_id'][0]

# Fill missing scores if any
scores[score_col] = scores[score_col].fillna(scores[score_col].mean())

if 'major' in students.columns:
    students['major'] = students['major'].fillna('Unknown')

# Merge the two datasets
merged_df = pd.merge(students, scores, on='student_id', how='inner')
print("\n--- Merged Dataset Preview ---")
print(merged_df.head())

# Calculate each student's average score
group_cols = ['student_id']
if 'name' in merged_df.columns:
    group_cols.append('name')

student_avg = merged_df.groupby(group_cols)[score_col].mean().round(2).reset_index()
student_avg.rename(columns={score_col: 'average_score'}, inplace=True)

print("\n--- Student Average Scores ---")
print(student_avg.head())

# Find the top 5 students
top_5_students = student_avg.sort_values(by='average_score', ascending=False).head(5)
print("\n--- Top 5 Students ---")
print(top_5_students.to_string(index=False))

# Compute average score by major
if 'major' in merged_df.columns:
    major_avg = merged_df.groupby('major')[score_col].mean().round(2).reset_index()
    major_avg.rename(columns={score_col: 'average_score_by_major'}, inplace=True)
    major_avg.sort_values(by='average_score_by_major', ascending=False, inplace=True)

    print("\n--- Average Score by Major ---")
    print(major_avg.to_string(index=False))