 
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added successfully.")


 
def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist.")
    elif book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Book ID {book_id} borrowed successfully.")

 
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


 
def register_member(members, member_id):
    members.add(member_id)    
    print(f"Member {member_id} registered.")

 
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


 
def main():
    
    catalog = {}          # Dictionary
    borrowed_books = []   # List
    members = set()       # Set

    # Adding 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 103, "Machine Learning", "David Lee", 2021)
    add_book(catalog, 104, "AI Fundamentals", "Sophia Clark", 2022)

    print()

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)

    # Trying duplicate member
    register_member(members, 2)

    print("\nRegistered Members:", members)

    print()

    # Borrowing books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("\nBorrowed Books:", borrowed_books)

    print()

    # Returning one book
    return_book(borrowed_books, 101)

    print("\nBorrowed Books After Return:", borrowed_books)

    # Display available books
    show_available(catalog, borrowed_books)


# Run the program
main()