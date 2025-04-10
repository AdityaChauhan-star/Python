def add_contact(contact_list):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    contact_list[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts(contact_list):
    if not contact_list:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, details in contact_list.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 30)

def search_contact(contact_list):
    search_term = input("Enter the name or phone number to search: ")
    search_results = []
    for name, details in contact_list.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            search_results.append((name, details))

    if search_results:
        print("Search Results:")
        for name, details in search_results:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 30)
    else:
        print("No matching contacts found.")

def update_contact(contact_list):
    name = input("Enter the name of the contact to update: ")
    if name in contact_list:
        print(f"Current details for '{name}':")
        print(f"Phone: {contact_list[name]['phone']}")
        print(f"Email: {contact_list[name]['email']}")
        print(f"Address: {contact_list[name]['address']}")
        print("Enter new details:")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contact_list[name]['phone'] = phone
        contact_list[name]['email'] = email
        contact_list[name]['address'] = address
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contact_list):
    name = input("Enter the name of the contact to delete: ")
    if name in contact_list:
        del contact_list[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contact_list = {}

    print("Welcome to the Contact Management App!")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_contact(contact_list)
        elif choice == "2":
            view_contacts(contact_list)
        elif choice == "3":
            search_contact(contact_list)
        elif choice == "4":
            update_contact(contact_list)
        elif choice == "5":
            delete_contact(contact_list)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
