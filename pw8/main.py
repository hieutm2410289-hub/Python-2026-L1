from input import input_students, input_courses
from output import (
    list_students,
    list_courses,
    sort_students,
    export_students,
    export_courses,
    export_marks,
    query_students,
    save_all_data_async
)

students = input_students()
courses = input_courses()

marks_data = {}
for course in courses:
    print("\nCourse:", course.name())
    course.input(students)

for student in students:
    student.calculate_gpa(courses)
    marks_data[student.id()] = student.marks()

save_all_data_async(students, courses, marks_data)

students = sort_students(students)
list_students(students)
list_courses(courses)

export_students(students)
export_courses(courses)
export_marks(students)

query_students()