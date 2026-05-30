# LISTS IN PYTHON

fruits = ["apple", "banana", "mango"]

print(fruits)
print(type(fruits))


# INDEXING

fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])

# SLICING

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# MODIFY LIST

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)

# APPEND

fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)


# INSERT

fruits = ["apple", "banana"]

fruits.insert(1, "orange")

print(fruits)


# REMOVE

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)


# POP

numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)


# LENGTH

numbers = [1, 2, 3, 4, 5]

print(len(numbers))


# LOOPING

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)



# MEMBERSHIP

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" in fruits)


# SORT

numbers = [5, 1, 8, 2, 3]

numbers.sort()

print(numbers)


# REVERSE

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# COMBINE LISTS

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)


# LIST COMPREHENSION

squares = [x**2 for x in range(1, 6)]

print(squares)



# MAX AND MIN

numbers = [10, 5, 20, 15]

print(max(numbers))
print(min(numbers))

# SUM

numbers = [1, 2, 3, 4, 5]

print(sum(numbers))


# NESTED LIST

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0])
print(matrix[1][2])


# PRACTICE QUESTIONS

# 1. Create a list of 10 numbers
# 2. Find largest number in a list
# 3. Find smallest number in a list
# 4. Calculate sum of all elements
# 5. Remove duplicates from a list
# 6. Reverse a list
# 7. Sort a list
# 8. Count occurrences of an element
# 9. Check if item exists in a list
# 10. Create a list of squares from 1 to 20

