class Student:
    def __init__(self, name, marks):
        self.name = name          # Public attribute
        self.__marks = marks      # Private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100")

student = Student("Mary", 85)

print("Student:", student.name)
print("Marks:", student.get_marks())

student.set_marks(90)
print("Updated Marks:", student.get_marks())