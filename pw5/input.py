from domains.student import Student
from domains.course import Course


def input_students():
    students = []

    n = int(input("Number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        id = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")

        students.append(Student(id, name, dob))

    with open("students.txt", "w") as f:
        for student in students:
            f.write(
                student.id() + ","
                + student.name() + ","
                + student.dob() + "\n"
            )

    return students


def input_courses():
    courses = []

    n = int(input("\nNumber of courses: "))

    for i in range(n):
        print("\nCourse", i + 1)

        id = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credits: "))

        courses.append(Course(id, name, credit))

    with open("courses.txt", "w") as f:
        for course in courses:
            f.write(
                course.id() + ","
                + course.name() + ","
                + str(course.credit()) + "\n"
            )

    return courses