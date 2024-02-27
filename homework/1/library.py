from libraryitem import LibraryItem
class Library:
    def __init__(self, items: list[LibraryItem]):
        self.items = items

    def add_item(self, item: LibraryItem):
        self.items.append(item)

    def remove_item(self, item: LibraryItem):
        self.items.remove(item)

    def display_items(self):
        y = f"The Items are: \n"
        for x in self.items:
            y += f"Item ID: {x.id} \nItem Title: {x.title} \nItem Avaibility: {x.available} \n \n"
        return y