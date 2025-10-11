from library_system import Book, EBook, PrintBook, Library

def main():

    my_library = Library()

    classic_book = Book("pride and prejudice", "jane austin")
    digital_novel = EBook("Snow crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The catcher in the Rye", "J.D Slinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ =="__main__":
    main()
