# STRINGS IN PYTHON

name = "Rahul"

print(name)
print(type(name))# STRINGS IN PYTHON

# ACCESSING CHARACTERS

text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n


# SLICING

text = "Python"

print(text[0:3])  # Pyt
print(text[2:6])  # thon
print(text[:4])   # Pyth
print(text[3:])   # hon



# LENGTH

text = "Python Programming"

print(len(text))



# CASE CONVERSION

text = "Python"

print(text.upper())
print(text.lower())


# STRIP

text = "   Hello World   "

print(text.strip())

# REPLACE

text = "I like Java"

print(text.replace("Java", "Python"))


# FIND

text = "Python Programming"

print(text.find("Programming"))


# IN OPERATOR

text = "Python Programming"

print("Python" in text)
print("Java" in text)

# SPLIT

text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)



# JOIN

words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print(sentence)



# CONCATENATION

first_name = "Rahul"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)



# F-STRINGS

name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")



# COUNT

text = "banana"

print(text.count("a"))



# REVERSE STRING

text = "Python"

print(text[::-1])



# PRACTICE QUESTIONS

# 1. Count vowels in a string
# 2. Reverse a string
# 3. Check if a string is palindrome
# 4. Count words in a sentence
# 5. Replace spaces with hyphens
# 6. Convert sentence to uppercase
# 7. Find frequency of a character
# 8. Check if a word exists in a sentence



