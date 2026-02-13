import json
from book import Book
from member import Member


class Library:
    """Main library management class"""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books:
            return "Book not found"

        if member_id not in self.members:
            return "Member not found"

        book = self.books[isbn]
        member = self.members[member_id]

        success, message = book.check_out(member_id)

        if success:
            member.borrow_book(isbn)

        return message

    def return_book(self, isbn, member_id):
        if isbn not in self.books or member_id not in self.members:
            return "Invalid book or member"

        book = self.books[isbn]
        member = self.members[member_id]

        book.return_book()
        member.return_book(isbn)

        return "Book returned successfully"

    def search_book(self, keyword):
        results = []
        for book in self.books.values():
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword == book.isbn
            ):
                results.append(book)
        return results

    def view_overdue_books(self):
        overdue_books = []
        for book in self.books.values():
            if book.is_overdue():
                overdue_books.append(book)
        return overdue_books

    def save_data(self):
        with open("data/books.json", "w") as f:
            json.dump(
                {isbn: book.to_dict() for isbn, book in self.books.items()},
                f,
                indent=4,
            )

        with open("data/members.json", "w") as f:
            json.dump(
                {mid: member.to_dict() for mid, member in self.members.items()},
                f,
                indent=4,
            )

    def load_data(self):
        try:
            with open("data/books.json", "r") as f:
                books_data = json.load(f)
                for isbn, data in books_data.items():
                    self.books[isbn] = Book.from_dict(data)
        except:
            pass

        try:
            with open("data/members.json", "r") as f:
                members_data = json.load(f)
                for mid, data in members_data.items():
                    self.members[mid] = Member.from_dict(data)
        except:
            pass
    def get_statistics(self):
    total_books = len(self.books)
    available_books = sum(1 for book in self.books.values() if book.available)
    borrowed_books = total_books - available_books
    total_members = len(self.members)
    overdue_books = sum(1 for book in self.books.values() if book.is_overdue())

    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "total_members": total_members,
        "overdue_books": overdue_books,
    }
