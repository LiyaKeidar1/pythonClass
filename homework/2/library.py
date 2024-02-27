class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def display_books(self):
        y = ''
        for k in self.book_list:
            y += f"\n {k} \n"
        return  y
                                
    def count_available_books(self):
        count = 0
        for y in self.book_list:
            if y.available:
                count += 1
        return count
