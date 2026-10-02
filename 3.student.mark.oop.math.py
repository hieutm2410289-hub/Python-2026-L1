import math
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.marks = {}

    def input(self):
        print("Student:", self.__name)

    def list(self):
        print(self.__id, self.__name, self.__dob,
              "GPA:", self.gpa())

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def gpa(self):
        if not self.marks:
            return 0

        total = 0
        credits = 0

        for mark, credit in self.marks.values():
            total += mark * credit
            credits += credit

        return total / credits


class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def input(self, students):
        for student in students:
            mark = float(input(
                "Mark for " + student.name() + ": "
            ))

            # Round down to 1 decimal
            mark = math.floor(mark * 10) / 10

            student.marks[self.__id] = (
                mark, self.__credit
            )

    def list(self):
        print(self.__id, self.__name,
              "-", self.__credit, "credits")

    def name(self):
        return self.__name


# Input students
students = []

n = int(input("Number of students: "))

for i in range(n):
    id = input("Student ID: ")
    name = input("Name: ")
    dob = input("DoB: ")

    students.append(Student(id, name, dob))


# Input courses
courses = []

n = int(input("Number of courses: "))

for i in range(n):
    id = input("Course ID: ")
    name = input("Course name: ")
    credit = int(input("Credits: "))

    courses.append(Course(id, name, credit))


# Input marks
for course in courses:
    print("\nCourse:", course.name())
    course.input(students)


# GPA using numpy
gpa_array = np.array([student.gpa() for student in students])


# Sort students by GPA descending
students = [
    student for _, student in
    sorted(
        zip(gpa_array, students),
        key=lambda x: x[0],
        reverse=True
    )
]


# List students
print("\n--- STUDENTS ---")

for student in students:
    student.list()


# List courses
print("\n--- COURSES ---")

for course in courses:
    course.list()