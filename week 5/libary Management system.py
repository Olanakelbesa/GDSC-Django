class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {'Available' if self.availability_status else 'Not Available'}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}, Name: {self.name}")
        if self.books_borrowed:
            print("Books Borrowed:")
            for book in self.books_borrowed:
                print(f"  - {book.title}")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book)
            book.availability_status = False
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.availability_status = True
            print(f"Book '{book.title}' returned successfully.")
        else:
            print(f"Book '{book.title}' is not borrowed by this user.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered successfully.")

    def borrow_book(self, user, book):
        user.borrow_book(book)
        transaction = Transaction(user, book, "Borrow")
        self.transactions.append(transaction)

    def return_book(self, user, book):
        user.return_book(book)
        transaction = Transaction(user, book, "Return")
        self.transactions.append(transaction)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_details()

    def display_users(self):
        print("Library Users:")
        for user in self.users:
            user.display_details()

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            transaction.display_details()


class Transaction:
    def __init__(self, user, book, action):
        self.user = user
        self.book = book
        self.action = action

    def display_details(self):
        print(f"Transaction: {self.user.name} {self.action} '{self.book.title}'")


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register User")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Users")
    print("7. Display Transactions")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == '2':
        name = input("Enter user name: ")
        user = User(len(library.users) + 1, name)
        library.register_user(user)

    elif choice == '3':
        library.display_books()
        user_id = int(input("Enter user ID: "))
        book_title = input("Enter book title to borrow: ")
        user = next((u for u in library.users if u.user_id == user_id), None)
        book = next((b for b in library.books if b.title == book_title), None)

        if user and book:
            library.borrow_book(user, book)
        else:
            print("Invalid user ID or book title.")

    elif choice == '4':
        library.display_books()
        user_id = int(input("Enter user ID: "))
        book_title = input("Enter book title to return: ")
        user = next((u for u in library.users if u.user_id == user_id), None)
        book = next((b for b in library.books if b.title == book_title), None)

        if user and book:
            library.return_book(user, book)
        else:
            print("Invalid user ID or book title.")

    elif choice == '5':
        library.display_books()

    elif choice == '6':
        library.display_users()

    elif choice == '7':
        library.display_transactions()

    elif choice == '8':
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
