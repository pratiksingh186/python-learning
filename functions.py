# FUNCTIONS IN PYTHON

def greet():
    print("Hello, Welcome to Python!")

greet()


# PARAMETERS

def greet(name):
    print(f"Hello, {name}")

greet("Rahul")



# MULTIPLE PARAMETERS

def add(a, b):
    print(a + b)

add(10, 20)



# RETURN

def add(a, b):
    return a + b

result = add(5, 7)

print(result)

# KEYWORD ARGUMENTS

def student(name, age):
    print(name, age)

student(age=20, name="Rahul")


# DEFAULT ARGUMENTS

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Rahul")

# *ARGS

def add_numbers(*numbers):
    print(sum(numbers))

add_numbers(1, 2, 3, 4, 5)
# **KWARGS

def display_info(**info):
    print(info)

display_info(name="Rahul", age=20)



# VARIABLE SCOPE

x = 100

def show():
    x = 50
    print(x)

show()
print(x)




# LAMBDA

square = lambda x: x * x

print(square(5))



# RECURSION

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)




# FACTORIAL

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))



# USER INPUT

def square(number):
    return number ** 2

num = int(input("Enter a number: "))

print(square(num))



# EVEN OR ODD

def check_even(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"

print(check_even(8))



# MAXIMUM OF TWO NUMBERS

def maximum(a, b):
    return max(a, b)

print(maximum(10, 20))



# PRACTICE QUESTIONS

# 1. Create a function to find square of a number
# 2. Create a function to find cube of a number
# 3. Create a function to check prime number
# 4. Create a function to find factorial
# 5. Create a function to reverse a string
# 6. Create a function to count vowels
# 7. Create a calculator using functions
# 8. Create a function to find largest number in a list
# 9. Create a function to check palindrome
# 10. Create a function to generate multiplication table

