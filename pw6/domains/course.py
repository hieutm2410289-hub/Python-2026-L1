import math
import pickle
import gzip


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
        try:
            with gzip.open("marks.pkl.gz", "rb") as f:
                marks = pickle.load(f)
        except FileNotFoundError:
            marks = {}

        if self.__id not in marks:
            marks[self.__id] = {}

        for student in students:
            mark = float(
                input("Mark for " + student.name() + ": ")
            )

            mark = math.floor(mark * 10) / 10

            student.marks[self.__id] = (
                mark,
                self.__credit
            )

            marks[self.__id][student.id()] = mark

        with gzip.open("marks.pkl.gz", "wb") as f:
            pickle.dump(marks, f)

    def list(self):
        print(
            self.__id,
            self.__name,
            "-",
            self.__credit,
            "credits"
        )