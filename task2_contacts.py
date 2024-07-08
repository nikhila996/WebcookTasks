contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added {name} with number {number}")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found in contacts")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts")
    else:
        print(f"{name} not found in contacts")

def list_contacts():
    print("Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

# Example usage:
add_contact("Alice", "1234567890")
add_contact("Bob", "9876543210")
list_contacts()
search_contact("Alice")
delete_contact("Bob")
list_contacts()
