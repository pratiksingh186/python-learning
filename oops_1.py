# OBJECT ORIENTED PROGRAMMING (OOP)

# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Creating objects
student1 = Student("Rahul", 20)
student2 = Student("Rohan", 21)

# Calling methods
student1.display_info()

print()

student2.display_info()



# CAR CLASS

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")


car1 = Car("Toyota", "Fortuner")

car1.start()



# MODIFY ATTRIBUTES

class Student:

    def __init__(self, name):
        self.name = name


student = Student("Rahul")

print(student.name)

student.name = "Rohan"

print(student.name)



# MULTIPLE OBJECTS

class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Tommy")
dog2 = Dog("Rocky")

dog1.bark()
dog2.bark()




# PRACTICE QUESTIONS

# 1. Create a Book class
# 2. Create a Mobile class
# 3. Create a BankAccount class
# 4. Create an Employee class
# 5. Create a Movie class
# 6. Create a Laptop class
# 7. Create a Rectangle class with area method
# 8. Create a Circle class with circumference method




# ==========================================
# OOP BASICS - CLASSES AND OBJECTS
# ==========================================

# Class:
# A blueprint used to create objects.

# Object:
# An instance of a class.

# Constructor:
# __init__() runs automatically when an object is created.

# self:
# Refers to the current object.

# Attributes:
# Variables inside a class.
# Example: self.name, self.age

# Methods:
# Functions inside a class.
# Example: display_info()

# Benefits of OOP:
# - Better code organization
# - Reusability
# - Easier maintenance
# - Real-world modeling



