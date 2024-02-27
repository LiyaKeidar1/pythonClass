from libraryitem import LibraryItem
from book import Book
from DVD import DVD
from library import Library

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book1 = Book("Liya Keidar", 1, "Super Yoda", True)
    DVD1 = DVD("Yossi Mor", 2, "The Amazing Life", True)
    newLib = Library([book1, DVD1])
    print(newLib.display_items())



    while True:
        x= int(input("CHOOSE FROM MENU: \n 1. Borrow an item \n 2. Return an item \n 3. Exit \n"))
        if x == 1:
            y = int(input("Enter item ID: "))
            for s in newLib.items:
                if y == s.id:
                    if s.available:
                        s.available = False
                        print(f"'{s.title}'1 has been borrowed")
                    else:
                        s.available = True
                        print(f"'{s.title}' has been returned")


        if x == 2:
            y = int(input("Enter item ID: "))
            for s in newLib.items:
                if y == s.id:
                    if not s.available:
                        s.available = True
                        print(f"'{s.title}' has been returned")

        if x == 3:
            print("Exiting...")
            break