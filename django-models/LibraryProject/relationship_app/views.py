from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryBookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs.get('library_id')
        if library_id:
            return Book.objects.filter(library_id=library_id)
        return Book.objects.all()
    

