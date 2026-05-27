# CONDITIONS IN PYTHON

# IF 

age = 18

if age >= 18:
    print("You are eligible to vote")


# IF ELSE

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# IF ELIF ELSE

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# COMPARISON OPERATORS

a = 18
b = 66

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# LOGICAL OPERATORS

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")



# OR OPERATOR

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You can relax")



# NOT OPERATOR

logged_in = False

if not logged_in:
    print("Please login")




# NESTED CONDITIONS

age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")



# USER INPUT WITH CONDITIONS

number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")




# PRACTICE QUESTIONS

# 1. Check if a person is eligible to vote
# 2. Find largest among 3 numbers
# 3. Check if number is positive or negative
# 4. Create simple login system
# 5. Check leap year
# 6. Check if number is divisible by 5 and 11

