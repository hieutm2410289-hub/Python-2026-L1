
students = []
courses = []
marks = {}

# Input students
n = int(input("Number of students: "))
for i in range(n):
    id = input("Student ID: ")
    name = input("Name: ")
    dob = input("DoB: ")
    students.append([id, name, dob])

# Input courses
n = int(input("Number of courses: "))
for i in range(n):
    id = input("Course ID: ")
    name = input("Course name: ")
    courses.append([id, name])

# Input marks
for course in courses:
    print("\nCourse:", course[1])
    marks[course[0]] = {}

    for student in students:
        mark = float(input("Mark for " + student[1] + ": "))
        marks[course[0]][student[0]] = mark

# List students
print("\n--- Students ---")
for s in students:
    print(s[0], s[1], s[2])

# List courses
print("\n--- Courses ---")
for c in courses:
    print(c[0], c[1])

# Show marks
print("\n--- Marks ---")
for course in courses:
    print("\n", course[1])
    for student in students:
        print(
            student[1],
            ":",
            marks[course[0]][student[0]]
        )
