from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int>:pk/', LibraryDetailView.as_view(), name='library_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
]
