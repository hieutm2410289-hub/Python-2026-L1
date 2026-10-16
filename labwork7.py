# 2.student.mark.oop.py

class Entity:
    """Base class representing a general entity (Encapsulation & Polymorphism)"""
    def __init__(self, entity_id="", name=""):
        self._id = entity_id      # Protected attribute
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def input(self):
        """Input method intended to be overridden in subclasses"""
        self._id = input("Enter ID: ")
        self._name = input("Enter Name: ")

    def list(self):
        """List method intended to be overridden in subclasses"""
        print(f"ID: {self._id} | Name: {self._name}")


class Student(Entity):
    """Student class inheriting from Entity"""
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob  # Private attribute

    def get_dob(self):
        return self.__dob

    # Overriding input method (Polymorphism)
    def input(self):
        self._id = input("  - Student ID: ")
        self._name = input("  - Student Name: ")
        self.__dob = input("  - Date of Birth (DoB): ")

    # Overriding list method (Polymorphism)
    def list(self):
        print(f"[Student] ID: {self._id:<10} | Name: {self._name:<20} | DoB: {self.__dob}")


class Course(Entity):
    """Course class inheriting from Entity"""
    def __init__(self, course_id="", name=""):
        super().__init__(course_id, name)

    # Overriding input method (Polymorphism)
    def input(self):
        self._id = input("  - Course ID: ")
        self._name = input("  - Course Name: ")

    # Overriding list method (Polymorphism)
    def list(self):
        print(f"[Course] ID: {self._id:<10} | Name: {self._name}")


class MarkManager:
    """Manager class handling continuous execution flow"""
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Format: {course_id: {student_id: mark}}

    def input_all(self):
        """Sequential input routine running without any menu choice"""
        
        # 1. Input Students
        print("\n================ 1. INPUT STUDENT INFORMATION ================")
        count_s = int(input("Enter number of students: "))
        for i in range(count_s):
            print(f"\n--- Enter Student #{i + 1} ---")
            s = Student()
            s.input()
            self.__students.append(s)

        # 2. Input Courses
        print("\n================ 2. INPUT COURSE INFORMATION ================")
        count_c = int(input("Enter number of courses: "))
        for i in range(count_c):
            print(f"\n--- Enter Course #{i + 1} ---")
            c = Course()
            c.input()
            self.__courses.append(c)

        # 3. Input Marks for each course
        print("\n================ 3. INPUT MARKS ================")
        for c in self.__courses:
            print(f"\n--- Enter marks for course: {c.get_name()} (ID: {c.get_id()}) ---")
            self.__marks[c.get_id()] = {}
            for s in self.__students:
                mark = float(input(f"  + Mark for {s.get_name()} (ID: {s.get_id()}): "))
                self.__marks[c.get_id()][s.get_id()] = mark

    def show_all_results(self):
        """Displays all stored data after inputs are complete"""
        print("\n=================== SUMMARY RESULTS ===================")
        
        # Display Student List
        print("\n--- STUDENT LIST ---")
        for s in self.__students:
            s.list()

        # Display Course List
        print("\n--- COURSE LIST ---")
        for c in self.__courses:
            c.list()

        # Display Mark Sheets
        print("\n--- DETAILED MARK SHEET ---")
        for c in self.__courses:
            c_id = c.get_id()
            print(f"\n* Course: {c.get_name()} (ID: {c_id})")
            for s in self.__students:
                mark = self.__marks[c_id].get(s.get_id(), "N/A")
                print(f"  + Student: {s.get_name():<20} | ID: {s.get_id():<10} | Mark: {mark}")

    def run(self):
        """Executes the complete pipeline in a single pass"""
        self.input_all()
        self.show_all_results()
        print("\nProgram finished successfully!")


if __name__ == "__main__":
    app = MarkManager()
    app.run()