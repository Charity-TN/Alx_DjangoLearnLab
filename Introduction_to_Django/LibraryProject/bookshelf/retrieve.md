```python
from bookshelf.models import Book                                            }")
if book:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Publication Year: {book.publication_year}")
else:
    print("No books found in the database.")

#Expected output
Title: 1984
Author: George Orwell
Publication Year: 1949