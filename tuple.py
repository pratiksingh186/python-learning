# TUPLES IN PYTHON

fruits = ("apple", "banana", "mango")

print(fruits)
print(type(fruits))


# INDEXING

fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
print(fruits[-1])


# SLICING

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# LENGTH

numbers = (10, 20, 30, 40)

print(len(numbers))


# LOOPING

fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)



# CONCATENATION

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)



# REPETITION

numbers = (1, 2)

print(numbers * 3)




# COUNT

numbers = (1, 2, 3, 1, 1)

print(numbers.count(1))




# INDEX

fruits = ("apple", "banana", "mango")

print(fruits.index("banana"))


# UNPACKING

person = ("Rahul", 20, "Bangalore")

name, age, city = person

print(name)
print(age)
print(city)


# SINGLE ELEMENT TUPLE

number = (10,)

print(type(number))


# LIST TO TUPLE

numbers = [1, 2, 3, 4]

new_tuple = tuple(numbers)

print(new_tuple)


# TUPLE TO LIST

numbers = (1, 2, 3)

new_list = list(numbers)

print(new_list)

# TUPLES ARE IMMUTABLE

fruits = ("apple", "banana", "mango")

# fruits[0] = "orange"
# This will cause an error



# PRACTICE QUESTIONS

# 1. Create a tuple of 5 favorite movies
# 2. Print first and last element
# 3. Count occurrences of a number
# 4. Find index of an element
# 5. Unpack a tuple into variables
# 6. Convert tuple to list and back
# 7. Find maximum and minimum value in a tuple
# 8. Check if an item exists in a tuple

