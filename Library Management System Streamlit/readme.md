# Library Management System

The Library Management System is a modular, Streamlit-based web application developed using Python and Object-Oriented Programming (OOP) principles. It allows you to manage books, users, and their borrowing activities through an interactive web interface.

## Overview
This Streamlit application provides an easy-to-use UI to manage a library. It includes three core classes:

**Example Usage:**

```
Program Options:
 1) Add book
 2) Print library books
 3) Print books by prefix
 4) Add user
 5) Borrow book
 6) Return book
 7) Print users borrowed book
 8) Print users
   
   ```

### Book
The `Book` class represents a book in the library and includes the following attributes:

- `id`: Unique identifier for the book.
- `name`: Title of the book.
- `quantity`: Number of copies available.

### User
The `User` class represents a library user and includes the following attributes:

- `id`: Unique identifier for the user.
- `name`: Name of the user.

### Admin
The `Admin` class manages the library system and provides various functionalities, including:

- Adding new books to the library.
- Printing all available books.
- Searching for books by name.
- Adding new users to the system.
- Borrowing books.
- Returning books.
- Printing users who borrowed books.
- Printing all users in the system.


# Features

- **Add Books**: Easily add new books to the library with unique IDs.
- **Manage Users**: Add new users to the system for tracking borrowing activities.
- **Search Books**: Search for books by name using a prefix.
- **Borrow and Return**: Borrow books from the library and return them when done.
- **Track Borrowers**: Keep track of users who have borrowed books.
- **User Interface**: Simple UI interface for user interaction.

- **Streamlit UI**: Interactive and dynamic web interface.

## Folder Structure:

**Create a folder for your project (e.g., LibraryManagementSystem/), and inside that, you will later add these files:**

library-management/
│
├── app.py                     # Main Streamlit app (UI logic)
│
├── models/
│   ├── book.py                # Book class (data and logic)
│   └── user.py                # User class (data and logic)
│
└── library/
    └── admin.py              # Admin class (library controller)




