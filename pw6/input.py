import pickle
import gzip

from domains.student import Student
from domains.course import Course


def save(data, filename):
    with gzip.open(filename, "wb") as f:
        pickle.dump(data, f)


def input_students():
    students = []

    n = int(input("Number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        id = input("Student ID: ")
        name = input("Name: ")
        dob = input("DoB: ")

        students.append(Student(id, name, dob))

    save(students, "students.pkl.gz")

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

    save(courses, "courses.pkl.gz")

    return courses