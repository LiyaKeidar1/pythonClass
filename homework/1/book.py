from libraryitem import LibraryItem
class Book(LibraryItem):
    def __init__(self, author: str,id: int, title: str, avaliable: bool):
        LibraryItem.__init__(self, id, title, avaliable)
        self.author = author

