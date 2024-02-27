class Book:
    def __init__(self, title1, author1, publication_year1):
        self.title = title1
        self.author = author1
        self.publication_year = publication_year1
        self.available  = True

    def __str__(self):
        return f"Book '{self.title}': \n Author: {self.author} \n Publication year: {self.publication_year}"

    def borrow(self):
        if self.available == True:
            self.available = False
            print ("Book has been borrowed")

        else:
            print("Book isn't available")
    
    def return_book(self):
        self.available = True
        print("Book has been returned")
        
    @classmethod
    def build_book(cls, hello: str):
        booklist = hello.split(",")
        book1 = Book(*booklist)
        return book1

    @staticmethod
    def is_a_book():
