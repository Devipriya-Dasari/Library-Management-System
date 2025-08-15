# app.py

import streamlit as st
from library.admin import Admin

admin = Admin()

st.title("📚 Library Management System")

menu = st.sidebar.radio(
    "Select an option:",
    [
        "1) Add book",
        "2) Print library books",
        "3) Print books by prefix",
        "4) Add user",
        "5) Borrow book",
        "6) Return book",
        "7) Print users borrowed book",
        "8) Print users"
    ]
)

if menu == "1) Add book":
    st.header("Add a Book")
    book_id = st.text_input("Book ID")
    book_name = st.text_input("Book Name")
    book_quantity = st.number_input("Quantity", min_value=1, step=1)
    if st.button("Add Book"):
        if book_id and book_name and book_quantity > 0:
            msg = admin.add_book(book_id, book_name, book_quantity)
            st.success(msg) if not msg.startswith("Error") else st.error(msg)
        else:
            st.error("Please fill in all fields!")

elif menu == "2) Print library books":
    st.header("Library Books")
    st.text(admin.get_all_books())

elif menu == "3) Print books by prefix":
    st.header("Search Books by Prefix")
    prefix = st.text_input("Enter prefix")
    if prefix:
        books = admin.search_books(prefix)
        if books:
            st.write("Books found:")
            for b in books:
                st.write(f"- {b}")
        else:
            st.warning("No books found.")

elif menu == "4) Add user":
    st.header("Add User")
    user_id = st.text_input("User ID")
    user_name = st.text_input("User Name")
    if st.button("Add User"):
        if user_id and user_name:
            msg = admin.add_user(user_id, user_name)
            st.success(msg) if "added" in msg else st.warning(msg)
        else:
            st.error("Please fill in all fields!")

elif menu == "5) Borrow book":
    st.header("Borrow Book")
    user_id = st.text_input("User ID to borrow")
    book_name = st.text_input("Book Name to borrow")
    if st.button("Borrow"):
        if user_id and book_name:
            msg = admin.borrow_book(user_id, book_name)
            st.success(msg) if "borrowed" in msg else st.error(msg)
        else:
            st.error("Please fill in all fields!")

elif menu == "6) Return book":
    st.header("Return Book")
    user_id = st.text_input("User ID to return")
    book_name = st.text_input("Book Name to return")
    if st.button("Return"):
        if user_id and book_name:
            msg = admin.return_book(user_id, book_name)
            st.success(msg) if "returned" in msg else st.error(msg)
        else:
            st.error("Please fill in all fields!")

elif menu == "7) Print users borrowed book":
    st.header("Users & Borrowed Books")
    st.text(admin.print_users_borrowed_books())

elif menu == "8) Print users":
    st.header("All Users")
    st.text(admin.print_all_users())
