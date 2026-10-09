import pandas as pd


def list_students(students):
    print("\n--- STUDENTS ---")

    for student in students:
        student.list()


def list_courses(courses):
    print("\n--- COURSES ---")

    for course in courses:
        course.list()


def sort_students(students):
    return sorted(
        students,
        key=lambda student: student.gpa(),
        reverse=True
    )


def export_students(students):
    data = []

    for student in students:
        data.append({
            "id": student.id(),
            "name": student.name(),
            "dob": student.dob()
        })

    df = pd.DataFrame(data)
    df.to_csv("students.csv", index=False)


def export_courses(courses):
    data = []

    for course in courses:
        data.append({
            "id": course.id(),
            "name": course.name(),
            "credit": course.credit()
        })

    df = pd.DataFrame(data)
    df.to_csv("courses.csv", index=False)


def export_marks(students):
    data = []

    for student in students:
        for course_id, value in student.marks.items():
            data.append({
                "student_id": student.id(),
                "course_id": course_id,
                "mark": value[0]
            })

    df = pd.DataFrame(data)
    df.to_csv("marks.csv", index=False)


def query_students():
    df = pd.read_csv("students.csv")

    condition = input(
        'Enter condition, example: name == "John": '
    )

    try:
        print("\n--- QUERY RESULT ---")
        print(df.query(condition))
    except:
        print("Invalid query")