# models/user.py

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_name):
        self.borrowed_books.append(book_name)

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            return True
        return False
