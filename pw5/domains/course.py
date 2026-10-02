import math


class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def credit(self):
        return self.__credit

    def input(self, students):
        with open("marks.txt", "w") as f:
            for student in students:
                mark = float(
                    input("Mark for " + student.name() + ": ")
                )

                mark = math.floor(mark * 10) / 10

                student.marks[self.__id] = (
                    mark,
                    self.__credit
                )

                f.write(
                    student.id() + ","
                    + self.__id + ","
                    + str(mark) + "\n"
                )

    def list(self):
        print(
            self.__id,
            self.__name,
            "-",
            self.__credit,
            "credits"
        )