import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:")
print(password)


# ==========================================
# EXPLANATION OF THE CODE
# ==========================================

# 1. Imported the random module to select random characters.

# 2. Imported the string module to access:
#    - uppercase letters
#    - lowercase letters
#    - digits
#    - special characters

# 3. Created a function called generate_password()
#    which generates a random password.

# 4. Combined all available characters into one string
#    using:
#    string.ascii_letters
#    string.digits
#    string.punctuation

# 5. Used a loop to randomly select characters
#    until the desired password length is reached.

# 6. Stored the generated password in a variable.

# 7. Took password length as input from the user.

# 8. Called the function and generated a password.

# 9. Printed the generated password on the screen.

# CONCEPTS USED:
# - Functions
# - Loops
# - User Input
# - Strings
# - Random Module
# - Return Statement

