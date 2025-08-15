# models/book.py

class Book:
    def __init__(self, book_id, name, quantity):
        self.id = book_id
        self.name = name
        self.quantity = int(quantity)
        self.borrowed = 0

    def available(self):
        return self.quantity - self.borrowed

    def borrow(self):
        if self.available() > 0:
            self.borrowed += 1
            return True
        return False

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
            return True
        return False
