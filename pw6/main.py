from input import input_students, input_courses

from output import (
    list_students,
    list_courses,
    sort_students,
    export_students,
    export_courses,
    export_marks,
    query_students
)


students = input_students()

courses = input_courses()

for course in courses:
    print("\nCourse:", course.name())
    course.input(students)

students = sort_students(students)

list_students(students)

list_courses(courses)

# Export CSV
export_students(students)
export_courses(courses)
export_marks(students)

# Query students
query_students()