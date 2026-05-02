# Daily Journal Logger 

# step 1 : declare the file 
FILENAME = "journal.txt"

# Step 2: Add new journal entry
def addJournal():
    try:
        with open(FILENAME, 'a') as  file:
            entry = input("Enter your Journal\n")
            file.write(entry + "\n")
    except FileNotFoundError:
        print("File not found, Add a new journal file")

# Step 3: Read the journal entries
def readJournal():
    try:
        with open(FILENAME, 'r') as file:
            entries = file.readlines()
            for entry in entries:
                print(entry)
    except FileNotFoundError:
        print("File not found, Add a new journal file")

def searchJournal():
    try:
        with open(FILENAME, 'r') as file:
            entries = file.readlines()
            keyword = input("Enter a keyword to search in the journal\n")
            for entry in entries:
                if keyword in entry:
                    print(entry)
    except FileNotFoundError:
        print("File not found, Add a new journal file")
def deleteItem():
    try:
        with open(FILENAME, 'r') as file:
            entries = file.readlines()
            keyword = input("Enter a keyword to delete from the journal\n")
            with open(FILENAME, 'w') as file:
                for entry in entries:
                    if keyword not in entry:
                        file.write(entry)
    except FileNotFoundError:
        print("File not found, Add a new journal file")




def showMenu():
    print("1. Add Journal Entry")
    print("2. Read Journal Entries")
    print("3. Search Journal Entries")
    print("4. Delete Journal Entry")
    print("4. Exit")

while True:
        showMenu()
        choice = input("Enter your choice\n")
        if choice == '1':
            addJournal()
        elif choice == '2':
            readJournal()
        elif choice == '3':
            searchJournal()
        elif choice == '4':
            deleteItem()
        elif choice == '5':
            print("Exiting the journal application")
            break
        else:
            print("Invalid choice, please try again")


