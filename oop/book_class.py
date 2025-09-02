# oop/book_class.py

class Book:
    """
    A class representing a Book with title, author, and publication year.
    Demonstrates the use of Python magic methods: __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize a Book instance"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to indicate when a Book instance is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation (for users)"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation (for developers/recreation)"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
