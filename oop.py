# Object Oriented Programming - uses classes and objects
#class - a blueprint of an object
#objects - it is an instance of a class

#eg " I want to buy a CAR that is a Gwagon --Car(class) and Gwangon(object)
# YOU SHOULD ALWAYS FIRST START WITH THE CLASS AND THEN MOVE TO THE OBJECT

class Employee:
    def __init__(self, name, gender, position,  age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    def drive(self):
        print("Employee is driving.")

    def eat(self):
        print("Employee is eating.")


employee1=Employee("Mary", "Female", "CEO", 21)
print(employee1.name, employee1.gender, employee1.position, employee1.age)
employee1.drive()
employee1.eat()

employee2=Employee("Joe", "Male", "Manager",32)
print(employee2.name, employee2.gender,employee1.position, employee2.age)
employee2.drive()
employee2.eat()

employee3=Employee("Daniel", "Male", "HR", 25)
print(employee3.name, employee3.gender, employee3.position, employee3.age)
employee3.drive()
employee3.eat()
