# Library Management System

from datetime import datetime, timedelta
import json

#save and load library data to a json file
LIBRARY_FILE = "library.json"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def save_to_file(self):
        return {
            'title': self.title,
            'author': self.author,
            'is_borrowed': self.is_borrowed
        }

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books = []
        self.load_from_file()

        #load book data from a json file
    def load_from_file(self):
        try:
            with open(LIBRARY_FILE, 'r') as file:
                data = json.load(file)
                for book_data in data:
                    book = Book(book_data['title'], book_data['author'])
                    book.is_borrowed = book_data['is_borrowed']
                    self.books.append(book)
        except FileNotFoundError:
            print("Library data file not found. Starting with an empty library.")

    def save_library(self):
        with open(LIBRARY_FILE, 'w') as file:
            data = [book.save_to_file() for book in self.books]
            json.dump(data, file, indent=4)

    # delete a book from the json file
    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.save_library()
                print(f"Book '{title}' has been deleted from the library.")
                return
        print(f"Book '{title}' not found in the library.")


    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        self.save_library()
        print(f"Book '{title}' added to the library!")

        # View all book

    def view_book(self):
        if not self.books:
            print("The library is Empty, add a book!")
        else:
            print(f"\n---- Library Books---")
            for book in self.books:
                book.display_info()


                # borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Book '{title}' has been  borrowed. Enjoy Reading")
                self.save_library()
                return
        print(f"Book '{title}' is not available for borrowing")
            

    # Returning a book 

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{title}' has been returned. ")
                self.save_library()
                return
        print(f"Book '{title}' is not borrowed or is not in the library")

# search and retrieve a  particular book
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book '{title}' found in the library.")
                book.display_info()
                return
        print(f"Book '{title}' not found in the library.")

# book return deadline one week after borrowing
    def return_deadline(self, title, borrow_date):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                return_date = borrow_date + timedelta(days=7)
                print(f"Book '{title}' should be returned by {return_date.strftime('%Y-%m-%d')}.")
                return
        print(f"Book '{title}' is not currently borrowed.")
# Main program

library = Library()

while True:
    print( "\n----- Welcome to Library Management system!-----")
    print("1. Add Book")
    print("2. View Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search a Book")
    print("6. Check Return Deadline")
    print("7. Delete Book")
    print("8. Exit")

    choice = input("Enter your choice from (1-8): ").strip()
    if choice == '1':
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        library.add_book(title, author)
    elif choice == '2':
        library.view_book()
    elif choice == '3':
        title = input("Enter the title of the book you wish to borrow: ").strip()
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter the title of the work you wish to return:  ").strip()
        library.return_book(title)
    elif choice == '5':
        title  = input("Enter title of the book you wish to serach: ")
        library.search_book(title)
    elif choice == '6':
        return_date = input("Enter the borrow date (YYYY-MM-DD): ")
        try:
            borrow_date = datetime.strptime(return_date, '%Y-%m-%d')
            title = input("Enter the title of the book to check return deadline: ").strip()
            library.return_deadline(title, borrow_date) 
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    elif choice == '7':
        title = input("Enter the title of the book you wish to delete: ").strip()
        library.delete_book(title)
    elif choice == '8:':
        print("Goodbye!")
        break
    else:
        print("Invalid choice choose between (1-8)")