# Contact Management System

contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name} added to contacts.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Editing {name}'s contact:")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"{name}'s contact updated.")
    else:
        print(f"{name} not found in contacts.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact deleted.")
    else:
        print(f"{name} not found in contacts.")

def search_contact():
    name = input("Enter the name to search for: ")
    if name in contacts:
        print(f"Contact details for {name}: {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")

def view_all_contacts():
    print("All Contacts:")
    for name, details in contacts.items():
        print(f"{name}: {details}")

def main():
    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
