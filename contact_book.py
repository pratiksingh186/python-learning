'''Here's a solid beginner contact_book.py project using:
Dictionaries
Functions
Loops
Conditions
User Input'''



contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone

    print("Contact added successfully.")


def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts found.")
    else:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")





# ==========================================
# PROJECT: CONTACT BOOK
# ==========================================

# Features:
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Delete Contact
# 5. Exit Program

# Concepts Used:
# - Dictionaries
# - Functions
# - Loops
# - Conditions
# - User Input

# Dictionary Structure:
# {
#     "Rahul": "9876543210",
#     "Rohan": "9876543211"
# }

# Functions:
# add_contact()     -> Adds a new contact
# view_contacts()  -> Displays all contacts
# search_contact() -> Finds a contact
# delete_contact() -> Removes a contact

# The while loop keeps the menu running
# until the user chooses Exit.


