'''inheritance.py should teach:

What inheritance is
Parent class
Child class
Reusing methods
Overriding methods
super()'''


# INHERITANCE IN PYTHON

# Parent Class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child Class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()



# PERSON -> STUDENT

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Student(Person):

    def study(self):
        print("Student is studying")


student = Student("Rahul")

student.display()
student.study()



# METHOD OVERRIDING

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()





# SUPER KEYWORD

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


student = Student("Rahul", 20)

student.display()




# MULTI LEVEL INHERITANCE

class Grandparent:

    def show_grandparent(self):
        print("I am Grandparent")


class Parent(Grandparent):

    def show_parent(self):
        print("I am Parent")


class Child(Parent):

    def show_child(self):
        print("I am Child")


child = Child()

child.show_grandparent()
child.show_parent()
child.show_child()



# VEHICLE -> CAR

class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car is Driving")


car = Car()

car.start()
car.drive()




# PRACTICE QUESTIONS

# 1. Create Person -> Teacher
# 2. Create Vehicle -> Bike
# 3. Create Animal -> Cat
# 4. Create Employee -> Manager
# 5. Demonstrate method overriding
# 6. Demonstrate super()
# 7. Create a three-level inheritance example
# 8. Create Person -> Student -> CollegeStudent



# ==========================================
# INHERITANCE IN PYTHON
# ==========================================

# Inheritance allows one class to acquire
# properties and methods of another class.

# Parent Class (Base Class):
# The class being inherited from.

# Child Class (Derived Class):
# The class that inherits from another class.

# Benefits:
# - Code Reusability
# - Less Repetition
# - Easier Maintenance

# Method Overriding:
# Child class replaces parent's method.

# super():
# Used to access methods or constructor
# from the parent class.

# Types of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multi-Level Inheritance
# 4. Hierarchical Inheritance



