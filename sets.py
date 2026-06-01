# SETS IN PYTHON

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


# DUPLICATES REMOVED

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# ADD ELEMENT

fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)

# UPDATE SET

fruits = {"apple", "banana"}

fruits.update(["mango", "orange"])

print(fruits)

# REMOVE

fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)




# DISCARD

fruits = {"apple", "banana"}

fruits.discard("grapes")

print(fruits)

# POP

fruits = {"apple", "banana", "mango"}

removed_item = fruits.pop()

print("Removed:", removed_item)
print(fruits)


# LENGTH

numbers = {1, 2, 3, 4, 5}

print(len(numbers))




# LOOPING

fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)





# MEMBERSHIP

fruits = {"apple", "banana", "mango"}

print("apple" in fruits)
print("grapes" in fruits)



# UNION

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))




# INTERSECTION

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))






# DIFFERENCE

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.difference(set2))




# SYMMETRIC DIFFERENCE

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))


# REMOVE DUPLICATES FROM LIST

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)




# FROZENSET

numbers = frozenset([1, 2, 3])

print(numbers)


# PRACTICE QUESTIONS

# 1. Create a set of favorite movies
# 2. Add and remove elements
# 3. Find common elements between two sets
# 4. Find unique elements in two sets
# 5. Remove duplicates from a list using a set
# 6. Check if an element exists in a set
# 7. Find union of two sets
# 8. Find intersection of two sets
# 9. Find difference between two sets
# 10. Create a frozenset

