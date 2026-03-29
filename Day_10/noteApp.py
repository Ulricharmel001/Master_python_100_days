# # My note App
# #step 1 : declare note file
# FILE = "noteApp.txt"

# #step : show menu

# def showMenu():
#     print("\n----Note App Menu----")
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Delete All Notes")
#     print("4. Exit")

# #step 2 : add note
# def addNote():
#     note = input("Enter your note")
#     with open(FILE, 'a') as file:
#         file.write(note + '\n')
#     print("Note added successfully")
# # step 3: View note
# def viewNote():
#     try:
#         with open(FILE, 'r') as file:
#             content = file.read()
#             if content:
#                 print("----Your Notes----\n")
#                 print(content)
#             else:
#                 print("No notes found!")

#     except FileNotFoundError:
#         print("File not found")
# # step 4: delete note
# def deleteNotes():
#     confirm = input("Are you sure you want to clear your note(yes/no):\n")
#     if confirm.lower() == 'yes':
#         with open(FILE, 'w') as file:
#             file.write("")
#             print("All notes deleted")

# while True:
#     showMenu()
#     command = input("Enter your action betwent (1-4)")
#     if command == '1':
#         addNote()
#     elif command == '2':
#         viewNote()
#     elif command == '3':
#         deleteNotes()
#     elif command == '4':
#         print("Goodbye! Thank you for using note app")
#         break
#     else:
#         print(" Invalid input, chose between (1-4)")


# challenge : add delete note by index, add search note by keyword, add edit note by index, add note with timestamp, add  export note  to text file

# implement challenge : features all






from datetime import datetime


file_name = "noteApp.txt"

def show_menu():
    print("\n----Note App Menu----")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note by Index")
    print("4. Search Note by Keyword")
    print("5. Edit Note by Index")
    print("6. Export Notes to Text File")
    print("7. Clear Notes")
    print("8. Exit")

def add_note():
    from datetime import datetime
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, 'a') as file:
        file.write(f"{timestamp} - {note}\n")
    print("Note added successfully")

def view_notes():
    try:
        with open(file_name, 'r') as file:
            indexed_notes = [f"{index} . {line}" for index, line in enumerate(file.readlines())]
            if indexed_notes:
                print("----Your Notes----\n")
                print("".join(indexed_notes))
            else:
                print("No notes found!")
    except FileNotFoundError:
        print("File not found")

def delete_note_by_index():
    view_notes()
    index = int(input("Enter the index of the note to delete: "))
    with open(file_name, 'r') as file:
        notes = file.readlines()
    if 0 <= index < len(notes):
        del notes[index]
        with open(file_name, 'w') as file:
            file.writelines(notes)
        print("Note deleted successfully")
    
def search_note_by_keyword():
    keyword = input("Enter the keyword to search: ")
    with open(file_name, 'r') as file:
        notes = file.readlines()
    found_notes = [note for note in notes if keyword in note]
    if found_notes:
        print("----Search Results----\n")
        print("".join(found_notes))
    else:
        print("No notes found with the given keyword")

def export_notes_to_text_file():
    export_file_name = input("Enter the name of the export file (with .txt extension): ")
    with open(file_name, 'r') as file:
        content = file.read()
    with open(export_file_name, 'w') as export_file:
        export_file.write(content)
    print(f"Notes exported successfully to {export_file_name}")

def edit_note_by_index():
    view_notes()
    index = int(input("Enter the index of the note to edit: "))
    with open(file_name, 'r') as file:
        notes = file.readlines()
    if 0 <= index < len(notes):
        new_note = input("Enter the new note: ")
        notes[index] = new_note + '\n'
        with open(file_name, 'w') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.writelines(f"{timestamp} - {note}" for note in notes)
        print("Note edited successfully")
def clearNote():
    confirm = input("Are you sure you wish to clear your notes (yes/no) ?\n")
    if confirm.lower() == 'yes':
        print("All note deleted!")
        with open(file_name, 'w') as file:
            file.write("")
    else:
        print("Delete Cancel")
  
 

while True:
        show_menu()
        command = input("Enter your action between (1-8): ")
        if command == '1':
            add_note()
        elif command == '2':
            view_notes()
        elif command == '3':
            delete_note_by_index()
        elif command == '4':
            search_note_by_keyword()
        elif command == '5':
            edit_note_by_index() 
        elif command == '6':
            export_notes_to_text_file()
        elif command == '7':
            clearNote()
        elif command == '8':
            print("Goodbye! Thank you for using note app")
            break
        else:
            print("Invalid input, choose between (1-8)")