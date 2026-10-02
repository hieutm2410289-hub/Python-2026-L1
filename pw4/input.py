from domains.student import Student
from domains.course import Course


def input_students():
    students = []

    n = int(input("Number of students: "))

    for i in range(n):
        id = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")

        students.append(Student(id, name, dob))

    return students


def input_courses():
    courses = []

    n = int(input("Number of courses: "))

    for i in range(n):
        id = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credits: "))

        courses.append(Course(id, name, credit))

    return courses