import math
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domains.person import Person

class Student(Person):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0.0

    def dob(self):
        return self.__dob

    def marks(self):
        return self.__marks

    def gpa(self):
        return self.__gpa

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(float(mark) * 10) / 10.0

    def calculate_gpa(self, courses):
        total_credits = 0
        total_score = 0.0
        
        for course in courses:
            c_id = course.id()
            if c_id in self.__marks:
                credits = course.credits()
                total_score += self.__marks[c_id] * credits
                total_credits += credits

        if total_credits > 0:
            self.__gpa = round(total_score / total_credits, 2)
        else:
            self.__gpa = 0.0
            
        return self.__gpa