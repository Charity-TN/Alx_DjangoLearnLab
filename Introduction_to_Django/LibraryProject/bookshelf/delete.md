```python
from bookshelf.models import Book
#Deleted the book instance
book = Book.objects.get(title="Nineteen Eighty-Four") 
book.delete()

#Retrieving the deleted book
try:                                                  
    book = Book.objects.get(title="Nineteen Eighty-Four")
    print("Book still exists!")                       
except Book.DoesNotExist:
    print("Book successfully deleted.")

#Expected Output
Book successfully deleted.