from libraryitem import LibraryItem
class DVD(LibraryItem):
    def __init__(self, director: str,id: int, title: str, avaliable: bool):
        LibraryItem.__init__(self, id, title, avaliable)
        self.director = director
