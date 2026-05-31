# DICTIONARIES IN PYTHON

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Bangalore"
}

print(student)
print(type(student))

# ACCESS VALUES

student = {
    "name": "Rahul",
    "age": 20
}

print(student["name"])
print(student["age"])


# GET METHOD

student = {
    "name": "Rahul",
    "age": 20
}

print(student.get("name"))

# ADD ITEM

student = {
    "name": "Rahul",
    "age": 20
}

student["course"] = "Python"

print(student)



# UPDATE VALUE

student = {
    "name": "Rahul",
    "age": 20
}

student["age"] = 21

print(student)


# REMOVE ITEM

student = {
    "name": "Rahul",
    "age": 20
}

student.pop("age")

print(student)


# LENGTH

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Bangalore"
}

print(len(student))


# LOOP KEYS

student = {
    "name": "Rahul",
    "age": 20
}

for key in student:
    print(key)



# LOOP VALUES

student = {
    "name": "Rahul",
    "age": 20
}

for value in student.values():
    print(value)



# LOOP ITEMS

student = {
    "name": "Rahul",
    "age": 20
}

for key, value in student.items():
    print(key, ":", value)





# CHECK KEY

student = {
    "name": "Rahul",
    "age": 20
}

print("name" in student)
print("salary" in student)



# NESTED DICTIONARY

students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Rohan",
        "age": 21
    }
}

print(students["student1"]["name"])




# KEYS, VALUES, ITEMS

student = {
    "name": "Rahul",
    "age": 20
}

print(student.keys())
print(student.values())
print(student.items())

# USER INPUT

name = input("Enter name: ")
age = int(input("Enter age: "))

person = {
    "name": name,
    "age": age
}

print(person)



# PRACTICE QUESTIONS

# 1. Create a dictionary for a book
# 2. Create a dictionary for a student
# 3. Update a value in a dictionary
# 4. Remove a key from a dictionary
# 5. Print all keys
# 6. Print all values
# 7. Check if a key exists
# 8. Create a nested dictionary
# 9. Count frequency of characters in a string
# 10. Store marks of 5 subjects in a dictionary

