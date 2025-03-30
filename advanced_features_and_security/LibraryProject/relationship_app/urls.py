from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from .views import add_book, edit_book, delete_book, book_list
from . import views
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int>:pk/', LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('', book_list, name='book_list'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

]

