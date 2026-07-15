
class Library:

    book_count = 0


    def __init__(self):
        self.books = list()


    def add_book(self, book):
        self.books.append(book)
        Library.book_count += book.quantity


    @property
    def display_books(self):
        print("Books in the Library:")

        for book in self.books:
            print(book.display_info())



class Book:
    def __init__(self, title, author, year, quantity=1):
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity


    def display_info(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}'

    
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}'


class EBook(Book):
    def __init__(self, title, author, year, format_type, quantity=1):
        super().__init__(title, author, year, quantity)
        self.format_type = format_type


    def display_info(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity} Format: {self.format_type}'


    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity} Format: {self.format_type}'


class Customer:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = list()


    def borrow_book(self, book):
        if book.quantity > 0:
            self.borrowed_books.append(book)
            book.quantity -= 1
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            return 'Book isn\'t available, yet'


    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.quantity += 1
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
        
    
    def __str__(self):
        return f'{self.name} borrowed books:{self.borrowed_books}'



class LibraryManagementSystem:

    def __init__(self):
        self.library = Library()
        self.customers = list() 


    def register_customer(self, new_customer):
        self.customers.append(new_customer)
        print(f'Customer {new_customer.name} registered in the system.')


    def display_customer_books(self, customer):
        print(f'Books borrowed by {customer.name}:')

        for book in customer.borrowed_books:
                print(book.display_info())


    def display_all_books(self):
            self.library.display_books


    def display_all_customers(self):
        print(self.customers)



book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")

customer1 = Customer("Alice")
customer2 = Customer("Bob")

library_system = LibraryManagementSystem()

library_system.register_customer(customer1)
library_system.register_customer(customer2)

library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)

customer1.borrow_book(book1)
customer1.borrow_book(ebook1)
customer2.borrow_book(book2)

customer1.return_book(book1)
customer2.return_book(book1)

library_system.display_customer_books(customer1)

library_system.display_all_books()
