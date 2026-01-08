# Smart Library Management System (OOP + JSON)

A small, realistic **console-based** library management application built in **Python** using **Object-Oriented Programming**.

## Features
- Book hierarchy with **abstraction + inheritance** (`Book`, `PhysicalBook`, `EBook`)
- Members can borrow/return books (association)
- Loans created on successful borrow (composition)
- Library controller (aggregation, separation of concerns)
- Custom exceptions + friendly error messages
- Save/load state using **JSON** (`data.json`)
- Docstrings across classes and public methods
- Optional tests with `pytest`

## Project Structure
```
smart-library/
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
```

## How to Run
From the project root:
```bash
python main.py
```

## Example Usage
- Add a book (physical or ebook)
- Add a member
- Borrow and return books
- Save the library to `data.json`
- Load it back later

## Saving & Loading
In the menu:
- **Save library** writes to `data.json`
- **Load library** reads from `data.json`

You can also use the API directly:
```python
from library.library import Library
lib = Library()
lib.save_to_file("data.json")
lib.load_from_file("data.json")
```

## Run Tests (Optional Bonus)
Install pytest (if not installed):
```bash
pip install pytest
```

Run:
```bash
pytest -q
```

## Notes
- For simplicity, this implementation treats an **EBook** as borrowable by **one member at a time**.
  If your teacher allows, you can change that rule (e.g., unlimited ebook borrows).
