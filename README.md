Smart Library Management System
Student Information

Name: Joyti Prokash Dash Talukdar

Student ID: 2330769

Course: Object-Oriented Programming (Python)

Instructor: Andrey Krutauz

Project Type: Individual Final Project

Project Description

This project is a Smart Library Management System developed in Python using Object-Oriented Programming (OOP) principles.

The system is designed for a small public library and allows users to:

Add books (Physical Books and EBooks)

Register members

Borrow and return books

Track loans

Save and load library data using JSON

Interact with the system using a console-based menu

The main objective of this project is to demonstrate a clear understanding of core OOP concepts, proper object modeling, and basic data persistence.

OOP Concepts Demonstrated

The project demonstrates the following concepts covered in class:

Encapsulation (private attributes and properties)

Inheritance

Abstraction using an Abstract Base Class

Polymorphism

Composition (Loan class)

Association (Member and Book relationship)

Aggregation (Library as a system controller)

Magic methods (__str__, __eq__)

Custom exceptions

File input/output using JSON

Documentation using docstrings

Optional automated testing using pytest

Project Structure
SmartLibrary-2330769/
├── library/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── loan.py
│   ├── library.py
│   └── exceptions.py
├── tests/
│   └── test_library.py
├── main.py
├── README.md
├── data.json
└── .gitignore

How to Run the Application
Step 1: Open terminal in the project folder (Windows example)
cd /d C:\Users\HP\Downloads\SmartLibrary-2330769

Step 2: Run the program
python main.py


A menu will appear that allows interaction with the library system.

Console Menu Features

Add physical book

Add ebook

Add member

Borrow book

Return book

List books

List members

List loans

Save library data

Load library data

Exit program

The console menu does not contain business logic. All application logic is handled by the Library class.

Saving and Loading Data

Library data is saved in JSON format

File name: data.json

Data persists between program runs

Example:

library.save_to_file("data.json")
library.load_from_file("data.json")

Automated Testing (Optional Bonus)
Install pytest
pip install pytest

Run tests
pytest -q


Tests verify core functionality such as borrowing, returning, error handling, and JSON persistence.

Notes

EBooks are designed to be borrowed by one member at a time for simplicity.

Custom exceptions are used for clear error handling.

The project prioritizes readability and correctness over advanced Python features.

Submission

This project is submitted as an individual GitHub repository in accordance with the course requirements.
