# Simple Library System mastering inheritance and composition

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"    

class EBook(Book):
    def __init__ (self,title,author,file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):   
        return f"{self.title} by {self.author}, Size: {self.file_size}KB"

class PrintBook(Book):        
    def __init__(self,title,author,page_count):
        super().__init__(title, author)
        self.page_count = page_count  # number of pages

    def __str__(self):
        return f"print {self.title} by {self.author}, Pages: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)   # uses each object's __str__()
