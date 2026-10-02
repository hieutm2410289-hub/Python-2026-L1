
class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def list(self):
        print(self.__id, self.__name, self.__dob)


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.marks = {}

    def input(self, students):
        for student in students:
            mark = float(input("Mark for " + student.name() + ": "))
            self.marks[student.id()] = mark

    def list(self):
        print(self.__id, self.__name)

    def id(self):
        return self.__id

    def name(self):
        return self.__name


class Person:
    pass


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
    courses.append(Course(id, name))

# Input marks
for course in courses:
    print("\nCourse:", course.name())
    course.input(students)

# List students
print("\n--- Students ---")
for student in students:
    student.list()

# List courses
print("\n--- Courses ---")
for course in courses:
    course.list()

# Show marks
print("\n--- Marks ---")

for course in courses:
    print("\n", course.name())

    for student in students:
        print(
            student.name(),
            ":",
            course.marks[student.id()]
        )
