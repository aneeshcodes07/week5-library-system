from library import Library
from book import Book
from member import Member


def main():
    library = Library()
    library.load_data()

    while True:
        print("\n==============================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. View Overdue Books")
        print("7. Save & Exit")
        print("8. View Library Statistics")


        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year: ")

            book = Book(title, author, isbn, year)
            library.add_book(book)
            print("Book added successfully")

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")

            member = Member(name, member_id)
            library.register_member(member)
            print("Member registered successfully")

        elif choice == "3":
            isbn = input("Enter ISBN: ")
            member_id = input("Enter Member ID: ")
            print(library.borrow_book(isbn, member_id))

        elif choice == "4":
            isbn = input("Enter ISBN: ")
            member_id = input("Enter Member ID: ")
            print(library.return_book(isbn, member_id))

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            results = library.search_book(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found")

        elif choice == "6":
            overdue_books = library.view_overdue_books()
            if overdue_books:
                for book in overdue_books:
                    print(f"{book} - Overdue by {book.days_overdue()} days")
            else:
                print("No overdue books")

        elif choice == "7":
            library.save_data()
            print("Data saved. Exiting...")
            break
        
        elif choice == "8":
            stats = library.get_statistics()
            print("\nLibrary Statistics:")
            print(f"Total Books: {stats['total_books']}")
            print(f"Available Books: {stats['available_books']}")
            print(f"Borrowed Books: {stats['borrowed_books']}")
            print(f"Total Members: {stats['total_members']}")
            print(f"Overdue Books: {stats['overdue_books']}")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
