#Parent Class/ Super Class/ Base Class

class Animal:
    isMammal = True
    age = 3

    def movement(self):
        print("Animal is moving")

 #Child Class/ Sub Class/ Derived Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Meow! Meow! Meow!")