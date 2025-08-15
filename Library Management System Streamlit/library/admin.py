# library/admin.py

import streamlit as st
from models.book import Book
from models.user import User

class Admin:
    def __init__(self):
        if "books" not in st.session_state:
            st.session_state.books = {}
        if "users" not in st.session_state:
            st.session_state.users = {}

    def add_book(self, book_id, name, quantity):
        quantity = int(quantity)
        if book_id in st.session_state.books:
            book = st.session_state.books[book_id]
            if book.name != name:
                return f"Error: Book ID '{book_id}' already exists with a different name '{book.name}'."
            book.quantity += quantity
            return f"Added {quantity} copies to '{book.name}'. New total: {book.quantity}"
        st.session_state.books[book_id] = Book(book_id, name, quantity)
        return f"Book '{name}' added with {quantity} copies."

    def get_all_books(self):
        if not st.session_state.books:
            return "No books added yet."
        result = []
        for book in st.session_state.books.values():
            result.append(f"{book.name} (ID: {book.id}) — Available: {book.available()} / {book.quantity}")
        return "\n".join(result)

    def search_books(self, prefix):
        return [book.name for book in st.session_state.books.values() if book.name.lower().startswith(prefix.lower())]

    def add_user(self, user_id, name):
        if user_id in st.session_state.users:
            return "User ID already exists."
        st.session_state.users[user_id] = User(user_id, name)
        return f"User '{name}' added."

    def borrow_book(self, user_id, book_name):
        user = st.session_state.users.get(user_id)
        if not user:
            return "User not found."
        book = next((b for b in st.session_state.books.values() if b.name.lower() == book_name.lower()), None)
        if not book:
            return "Book not found."
        if book.borrow():
            user.borrow_book(book.name)
            return f"{user.name} borrowed '{book.name}'."
        return "No available copies to borrow."

    def return_book(self, user_id, book_name):
        user = st.session_state.users.get(user_id)
        if not user:
            return "User not found."
        book = next((b for b in st.session_state.books.values() if b.name.lower() == book_name.lower()), None)
        if not book:
            return "Book not found."
        if user.return_book(book.name):
            book.return_book()
            return f"{user.name} returned '{book.name}'."
        return f"{user.name} did not borrow '{book.name}'."

    def print_users_borrowed_books(self):
        if not st.session_state.users:
            return "No users found."
        result = []
        for user in st.session_state.users.values():
            books = ", ".join(user.borrowed_books) if user.borrowed_books else "No borrowed books"
            result.append(f"{user.name} (ID: {user.id}): {books}")
        return "\n".join(result)

    def print_all_users(self):
        if not st.session_state.users:
            return "No users found."
        return "\n".join(f"{user.name} (ID: {user.id})" for user in st.session_state.users.values())
