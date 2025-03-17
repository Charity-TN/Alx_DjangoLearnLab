```python
from bookshelf.models import Book                                            
book = Book.objects.get(id=1) 
print(f"Title: {book.title}, Author: {book.author}, Published in: {book.publication_year}")

#Expected Output
Title: 1984, Author: George Orwell, Published in: 1949