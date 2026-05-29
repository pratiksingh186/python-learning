# LOOPS IN PYTHON

# FOR LOOP

for i in range(5):
    print(i)


# FOR LOOP 1 TO 10

for i in range(1, 11):
    print(i)


# LOOP THROUGH LIST

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)



# WHILE LOOP

count = 1

while count <= 5:
    print(count)
    count += 1




# BREAK

for i in range(1, 11):
    if i == 6:
        break

    print(i)


# CONTINUE

for i in range(1, 11):
    if i == 5:
        continue

    print(i)



# NESTED LOOPS

for i in range(3):
    for j in range(3):
        print(i, j)




# TABLE OF 5

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")



# SUM OF FIRST 10 NUMBERS

total = 0

for i in range(1, 11):
    total += i

print(total)




# STAR PATTERN

for i in range(1, 6):
    print("*" * i)




# USER INPUT

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



# PRACTICE QUESTIONS

# 1. Print numbers from 1 to 100
# 2. Print even numbers from 1 to 50
# 3. Find sum of first 50 numbers
# 4. Print multiplication table of any number
# 5. Count digits in a number
# 6. Reverse a number
# 7. Print star triangle pattern
# 8. Print factorial of a number
# 9. Find largest number in a list
# 10. Create a number guessing game



