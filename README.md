# Library Management System

Welcome to the Library Management System! This application provides a command-line interface (CLI) for managing books, users, authors, and genres in a library. The system allows you to add new books, borrow and return books, search for books, and view details of users, authors, and genres.

# Features

- **Book Operations:**
  - Add a new book
  - Borrow a book
  - Return a book
  - Search for a book by title or ISBN
  - Display all books

- **User Operations:**
  - Add a new user
  - View user details
  - Display all users

- **Author Operations:**
  - Add a new author
  - View author details
  - Display all authors

- **Genre Operations:**
  - Add a new genre
  - View genre details
  - Display all genres

## Class Structure

### Book
Represents individual books with attributes:
- Title
- Author
- ISBN
- Genre
- Publication Date
- Availability Status

### Fiction Book and Non-Fiction Book
Inherits from the `Book` class and represents specialized book categories.

### User
Represents library users with attributes:
- Name
- Library ID
- List of Borrowed Book Titles

### Author
Represents book authors with attributes:
- Name
- Biography

### Genre
Represents book genres with attributes:
- Name
- Description
