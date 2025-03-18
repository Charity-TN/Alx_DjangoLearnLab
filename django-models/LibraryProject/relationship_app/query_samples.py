from relationship_app.models import Book, Library, Librarian

#Query all books by a specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author_name== author_name)

#List all books in a Library
def get_books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

#Retrieve the Librarian for a library
def get_librarian_for_library(library_name):
    return Librarian.objects.get(library_name=library_name)