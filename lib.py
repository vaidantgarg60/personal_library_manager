import json
import os

FILE_NAME = "library.json"

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Book(**book) for book in data]
    return []

def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump([book.to_dict() for book in library], file, indent=4)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year published: ")
    library.append(Book(title, author, year))
    print("✅ Book added!")

def view_books(library):
    if not library:
        print("Library is empty.")
        return
    print("\n📚 Your Books:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book}")

def search_books(library):
    keyword = input("Enter a keyword to search by title: ").lower()
    results = [book for book in library if keyword in book.title.lower()]
    if results:
        print("\n🔍 Search Results:")
        for book in results:
            print(f"- {book}")
    else:
        print("No books found.")

def delete_book(library):
    view_books(library)
    try:
        choice = int(input("Enter the number of the book to delete: "))
        removed = library.pop(choice - 1)
        print(f"❌ Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid selection.")

def main():
    library = load_library()

    while True:
        print("\n=== PERSONAL LIBRARY MANAGER ===")
        print("1. View Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            delete_book(library)
        elif choice == "5":
            save_library(library)
            print("📁 Library saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
