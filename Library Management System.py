


class Book:
    def __init__(self, title, author, isbn, genre, publication_date, available=True):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = available

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def genre(self):
        return self.__genre

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, status):
        self.__available = status

    def __str__(self):
        return f"{self.__title} by {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Published: {self.__publication_date}, Available: {self.__available}"


class FictionBook(Book):
    def __str__(self):
        return f"Fiction - {super().__str__()}"


class NonFictionBook(Book):
    def __str__(self):
        return f"Non-Fiction - {super().__str__()}"


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def library_id(self):
        return self.__library_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def __str__(self):
        return f"User: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(self.__borrowed_books)}"


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    def __str__(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"


class Genre:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    def __str__(self):
        return f"Genre: {self.__name}, Description: {self.__description}"


class LibraryCLI:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Please choose an option: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to main menu")
            choice = input("Please choose an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to main menu")
            choice = input("Please choose an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to main menu")
            choice = input("Please choose an option: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to main menu")
            choice = input("Please choose an option: ")

            if choice == '1':
                self.add_genre()
            elif choice == '2':
                self.view_genre_details()
            elif choice == '3':
                self.display_genres()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter publication date: ")
        new_book = Book(title, author, isbn, genre, publication_date)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def borrow_book(self):
        isbn = input("Enter the ISBN of the book to borrow: ")
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self):
        isbn = input("Enter the ISBN of the book to return: ")
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"You have returned '{book.title}'")
                else:
                    print("Book was not borrowed.")
                return
        print("Book not found.")

    def search_book(self):
        search_term = input("Enter the title or ISBN of the book to search for: ")
        for book in self.books:
            if book.title == search_term or book.isbn == search_term:
                print(book)
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter user library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User '{name}' added successfully!")

    def view_user_details(self):
        library_id = input("Enter user library ID: ")
        for user in self.users:
            if user.library_id == library_id:
                print(user)
                return
        print("User not found.")

    def display_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully!")

    def view_author_details(self):
        name = input("Enter author name: ")
        for author in self.authors:
            if author.name == name:
                print(author)
                return
        print("Author not found.")

    def display_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            print(author)

    def add_genre(self):
        name = input("Enter genre name: ")
        description = input("Enter genre description: ")
        new_genre = Genre(name, description)
        self.genres.append(new_genre)
        print(f"Genre '{name}' added successfully!")

    def view_genre_details(self):
        name = input("Enter genre name: ")
        for genre in self.genres:
            if genre.name == name:
                print(genre)
                return
        print("Genre not found.")

    def display_genres(self):
        if not self.genres:
            print("No genres available.")
        for genre in self.genres:
            print(genre)


if __name__ == "__main__":
    cli = LibraryCLI()
    cli.main_menu()
6