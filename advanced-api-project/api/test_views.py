from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.urls import reverse

# Create your tests here.
class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            author=self.author,
            publication_year=1997
        )
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        data = {
            "title": "The Hobbit",
            "author": self.author.id,
            "publication_year": 1937
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        data = {"title": "Harry Potter and the Philosopher's Stone"}
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        response = self.client.get(self.book_list_url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        response = self.client.get(self.book_list_url, {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_year(self):
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from rest_framework.authtoken.models import Token

    def test_unauthenticated_user_cannot_create_book(self):
        data = {"title": "Unauthorized Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {"title": "Authorized Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)