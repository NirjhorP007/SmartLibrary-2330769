"""Console menu interface for the Smart Library Management System."""

from library.book import PhysicalBook, EBook
from library.library import Library
from library.member import Member
from library.exceptions import LibraryError


def prompt(msg: str) -> str:
    """Prompt helper that strips input."""
    return input(msg).strip()


def print_header() -> None:
    print("\n=== Smart Library Management System ===")


def menu() -> None:
    """Run the console menu (no business logic here)."""
    lib = Library()
    data_file = "data.json"

    while True:
        print_header()
        print("1) Add physical book")
        print("2) Add ebook")
        print("3) Add member")
        print("4) Borrow book")
        print("5) Return book")
        print("6) List books")
        print("7) List members")
        print("8) List loans")
        print("9) Save library")
        print("10) Load library")
        print("0) Exit"ிப)
        choice = prompt("Choose an option: ")

        try:
            if choice == "1":
                book_id = prompt("Book ID: ")
                title = prompt("Title: ")
                author = prompt("Author: ")
                copies = int(prompt("Available copies: "))
                lib.add_book(PhysicalBook(book_id, title, author, copies))
                print("✅ Physical book added.")

            elif choice == "2":
                book_id = prompt("Book ID: ")
                title = prompt("Title: ")
                author = prompt("Author: ")
                size = float(prompt("File size (MB): "))
                lib.add_book(EBook(book_id, title, author, size))
                print("✅ EBook added.")

            elif choice == "3":
                member_id = prompt("Member ID: ")
                name = prompt("Name: ")
                lib.add_member(Member(member_id, name))
                print("✅ Member added.")

            elif choice == "4":
                member_id = prompt("Member ID: ")
                book_id = prompt("Book ID: ")
                loan = lib.borrow_book(member_id, book_id)
                print(f"✅ Borrowed successfully: {loan}")

            elif choice == "5":
                member_id = prompt("Member ID: ")
                book_id = prompt("Book ID: ")
                lib.return_book(member_id, book_id)
                print("✅ Returned successfully.")

            elif choice == "6":
                print("\n--- Books ---")
                for b in lib.list_books():
                    print(b)

            elif choice == "7":
                print("\n--- Members ---")
                for m in lib.list_members():
                    print(m)

            elif choice == "8":
                print("\n--- Loans ---")
                for l in lib.loans:
                    print(l)

            elif choice == "9":
                lib.save_to_file(data_file)
                print(f"✅ Saved to {data_file}.")

            elif choice == "10":
                lib.load_from_file(data_file)
                print(f"✅ Loaded from {data_file}.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("❌ Invalid option. Please try again.")

        except LibraryError as e:
            print(f"⚠️  {e}")
        except ValueError:
            print("⚠️  Invalid number format.")
        except OSError as e:
            print(f"⚠️  File error: {e}")


if __name__ == "__main__":
    menu()
