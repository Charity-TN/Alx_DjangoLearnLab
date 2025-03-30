```python
from bookshelf.models import Book
 
book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)      
book.save


## Expected Output:
print(f"Book Created: {book.title}, {book.author}, {book.publication_year}") 

#Successful Creation of the book instance
