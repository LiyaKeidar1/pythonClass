class LibraryItem:
    def __init__(self, id: int, title: str, avaliable: bool):
        self.id = id
        self.title= title
        self.available = avaliable

    def checkout(self):
        self.avalible = False

    def checkin(self):
        self.avalible = True
