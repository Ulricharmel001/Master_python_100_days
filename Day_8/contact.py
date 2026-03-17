# contact book
# step 1: innitialise an empyty book
contacts = {}
#step 1: display menu
def Show_menu():
    print("\n ---Contact Book Menu---")
    print("1. Add Contact ")
    print("2. View Contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete Contact")
    print("6. Exit ")


def addContact():
    name = input("Enter contact name")
    phone = input("Enter contact number:")
    email = input(" Enter contact Email")
    contacts[name] = {'email': email, 'phone': phone}
    print(f"contact {name}, has been added successfully")

def viewContact():
    if contacts:
        print('\n----Contact List---')
        for name, items in contacts.items():
            print(f"Name: {name}")
            print(f"Email: {items['email']}")
            print(f"Phone: {items['phone']}")
    else:
        print("You contact book is empty ")


def Searchcontact():
    name = input("input the name of the contact ")
    if name in contacts:
        print("\n--- contact detail for {name}----")
        print(f"Email: {contacts}[name]['email']")
        print(f"Phone:  {contacts}[name]['phone']")
    else:
        print(f"Contact {name} not found in your contact list!")

def EditContact():
    name = input("input the name of the contact you want to edit")
    if name in contacts:
        new_phone = input("Enter new phone number")
        new_email = input("Enter new email address")
        contacts[name]['phone'] = new_phone
        contacts[name]['email'] = new_email
        print(f"Contact {name} has been updated successfully")
    else:
        print(f"Contact {name} not found in your contact list!")


def deleteContact():
    name = input("input the name of the contact you want to delete")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found in your contact list!")


while True:
    Show_menu()
    choice = input("Enter your choice (1-6):")
    if choice == '1':
        addContact()
    elif choice == '2':
        viewContact()
    elif choice == '3':
        Searchcontact()
    elif choice == '4':
        EditContact()
    elif choice == '5':
        deleteContact()
    elif choice == '6':
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")