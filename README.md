Library Management System (Week 5 Internship Project)
📌 Project Description

This project is a console-based Library Management System built using Python and Object-Oriented Programming principles. It manages books, members, borrowing, returning, overdue tracking, and data persistence using JSON files.

🧠 OOP Concepts Used

Classes & Objects

Encapsulation

Constructors (init)

Class Methods

Dictionaries for fast lookup

File Handling (JSON)

Modular Structure

✨ Features

✔ Add and search books
✔ Register members
✔ Borrow & return books
✔ Due date tracking
✔ Overdue detection

How to run
```
cd week5-library-system
python -m library_system.main
```

Folder Structure
```
library_system/
    book.py
    member.py
    library.py
    main.py
data/
    books.json
    members.json
```

What I Learned

Designing real-world systems using OOP

Managing relationships between classes

Data persistence using JSON

Writing modular and maintainable code


Library statistics
✔ Data saved in JSON files
✔ Menu-driven interface# week5-library-system

Sample Menu
================================
    LIBRARY MANAGEMENT SYSTEM
================================
1. Add New Book
2. Register New Member
3. Borrow Book
4. Return Book
5. Search Books
6. View All Books
7. View All Members
8. View Overdue Books
9. Save & Exit
0. Exit Without Saving

Enter your choice:


Sample Output
Search Results for 'python':
----------------------------------------
1. Python Crash Course (ISBN: 9781593279288)
   Author: Eric Matthes
   Status: Available

2. Automate the Boring Stuff with Python (ISBN: 9781593275990)
   Author: Al Sweigart
   Status: Borrowed by John Doe (Due: 2024-02-15)

Library Statistics:
- Total Books: 125
- Available Books: 89
- Total Members: 45
- Books Borrowed: 36
- Overdue Books: 3
