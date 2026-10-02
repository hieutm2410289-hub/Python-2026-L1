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