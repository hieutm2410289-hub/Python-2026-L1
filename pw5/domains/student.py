import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.marks = {}

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def dob(self):
        return self.__dob

    def gpa(self):
        if not self.marks:
            return 0

        marks = np.array([x[0] for x in self.marks.values()])
        credits = np.array([x[1] for x in self.marks.values()])

        return np.sum(marks * credits) / np.sum(credits)

    def list(self):
        print(
            self.__id,
            self.__name,
            self.__dob,
            "GPA:",
            self.gpa()
        )