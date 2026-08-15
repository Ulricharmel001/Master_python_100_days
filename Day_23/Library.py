# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status ="Available" if not self.is_borrowed else "Borrowed"
        print(F"Tittle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}, added to the library!'")

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
                return
            print(f"Book '{title}', is not available for borrowing")

    # Returning a book 

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{title}' has been returned. ")
                return
            print(f"Book '{title}', is not in the library  ")

# Main program

library = Library()

while True:
    print( "\n----- Welcome to Library Management system!-----")
    print("1. Add Book")
    print("2. View Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter  your choice from (1-5):").strip()
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice choose between (1-5)")