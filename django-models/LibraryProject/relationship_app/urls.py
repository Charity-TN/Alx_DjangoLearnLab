from django.urls import path
from relationship_app import list_books, LibraryDetailView, views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int>:pk/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),

]
