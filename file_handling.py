# FILE HANDLING IN PYTHON

# CREATE AND WRITE TO A FILE

file = open("sample.txt", "w")

file.write("Hello World\n")
file.write("Learning Python File Handling")

file.close()


# READ FILE

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# READ LINE BY LINE

file = open("sample.txt", "r")

for line in file:
    print(line)

file.close()

# APPEND DATA

file = open("sample.txt", "a")

file.write("\nThis line was appended.")

file.close()


# USING WITH

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)



# COUNT WORDS

with open("sample.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

print("Total words:", word_count)



# COUNT LINES

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))




# USER INPUT TO FILE

name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write(name + "\n")





# PRACTICE QUESTIONS

# 1. Create a file and write your bio
# 2. Read and display file contents
# 3. Count words in a file
# 4. Count lines in a file
# 5. Store 5 names entered by user
# 6. Copy contents from one file to another
# 7. Find how many times a word appears in a file

