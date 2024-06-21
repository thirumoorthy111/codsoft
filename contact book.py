contacts = {}

def add_contact(name, number, email, address):
    contacts[name] = {
        'number': number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    if name in contacts:
        contact_details = contacts[name]
        print(f"Name: {name}")
        print(f"Number: {contact_details['number']}")
        print(f"Email: {contact_details['email']}")
        print(f"Address: {contact_details['address']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def print_contacts():
    if contacts:
        print("Contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Number: {details['number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("---------------------")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. Print all contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            name = input("Enter contact name: ").strip()
            number = input("Enter contact number: ").strip()
            email = input("Enter contact email: ").strip()
            address = input("Enter contact address: ").strip()
            add_contact(name, number, email, address)
        elif choice == '2':
            name = input("Enter contact name to search: ").strip()
            search_contact(name)
        elif choice == '3':
            name = input("Enter contact name to delete: ").strip()
            delete_contact(name)
        elif choice == '4':
            print_contacts()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
