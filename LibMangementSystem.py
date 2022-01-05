class Library:
    def __init__(self, list_of_books):  
        self.available_books = list_of_books
    
    def display(self):
        print("Available books in library are: ")
        for book in self.available_books:
            print(book)
    def lend_book(self,requested_book):
        if requested_book in self.available_books:
            print("You have now borrowed the book ")
            self.available_books.remove(requested_book)
        else:
            print("You already buyed that book")
    def add_book(self,book):
        if book in self.available_books:
            print("We already have this book")
        else:
            print("Thank you for the book")
            self.available_books.append(book)
            
class Customer:
    def request_book(self):
        self.book = input("Enter the name of the book you want: ")
        return self.book
    def return_book(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    
library = Library(["Harry Potter", "pride", "biology", "Computer Science", "Object Oriented Programming"])
customer = Customer()

while True:
    print("Enter 1 to display books")
    print("Enter 2 to lend a book")
    print("Enter 3 to return a book")
    print("Enter 4 to quit")
    
    user_choice = int(input())
    
    if user_choice == 1:
        library.display()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice == 4:
        break