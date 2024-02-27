from book import Book
class Novel(Book):
    def __init__(self, title, author, publication_year, genre: str):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def __str__(self):
        return f"Novel '{self.title}': \n Author: {self.author} \n Publication year: {self.publication_year} \n Genre: {self.genre}"
    
