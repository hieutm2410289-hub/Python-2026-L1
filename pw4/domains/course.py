import math


class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def name(self):
        return self.__name

    def input(self, students):
        for student in students:
            mark = float(input(
                "Mark for " + student.name() + ": "
            ))

            mark = math.floor(mark * 10) / 10
            student.marks[self.__id] = (
                mark,
                self.__credit
            )

    def list(self):
        print(
            self.__id,
            self.__name,
            "-",
            self.__credit,
            "credits"
        )