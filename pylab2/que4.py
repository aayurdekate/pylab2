# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        """Add a book to the library."""
        if isbn in self.books:
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def get_book_details(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        return self.books.get(isbn, f"No book found with ISBN {isbn}.")

    def search_books(self, search_term):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_all_books(self):
        """List all books currently in the library."""
        return self.books

    def update_book_details(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        """Update the details of an existing book."""
        if isbn in self.books:
            if title:
                self.books[isbn]['title'] = title
            if author:
                self.books[isbn]['author'] = author
            if publisher:
                self.books[isbn]['publisher'] = publisher
            if volume:
                self.books[isbn]['volume'] = volume
            if year:
                self.books[isbn]['year'] = year
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

# Sample Data
library_manager = LibraryManager()

# Adding books
library_manager.add_book('978-0134685991', 'Operating Systems: Principles and Practice', 'William Stallings', 'Pearson', '1st', 2021)
library_manager.add_book('978-0134685992', 'Introduction to Data Structures and Algorithms', 'Michael T. Goodrich', 'Wiley', '2nd', 2022)
library_manager.add_book('978-0134685993', 'Machine Learning with Python', 'Mark E. Fenner', 'O\'Reilly Media', '3rd', 2023)

# Removing a book
library_manager.remove_book('978-0134685992')

# Retrieving a book's details
print("Details of ISBN 978-0134685991:", library_manager.get_book_details('978-0134685991'))

# Searching for books
print("Search results for 'Machine Learning':", library_manager.search_books('Machine Learning'))

# Listing all books
print("All books in the library:", library_manager.list_all_books())

# Updating a book's details
library_manager.update_book_details('978-0134685991', title='Advanced Operating Systems')

# Checking availability of a book
print("Check availability for ISBN 978-0134685991:", library_manager.check_availability('978-0134685991'))
print("Check availability for ISBN 978-0134685992:", library_manager.check_availability('978-0134685992'))
