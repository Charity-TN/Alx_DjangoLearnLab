from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_book.html', {'books':books})

from django.views.generic import ListView


class LibraryBookListView(ListView):
    model = Book
    template_name = 'library_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs.get('library_id')
        return Book.objects.filter(library_id=library_id)
    

