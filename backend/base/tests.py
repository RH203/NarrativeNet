from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Genre, Chapter, Author
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

class TestBookViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
    def test_get_books(self):
        # Test retrieving books without authentication
        response = self.client.get(reverse('get_books'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test retrieving books with authentication
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('get_books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to check the response data
    def test_get_books_by_genre(self):
        # Test retrieving books by genre without authentication
        response = self.client.get(reverse('get_books_by_genre', kwargs={'genre_name': 'fantasy'}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test retrieving books by genre with authentication
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('get_books_by_genre', kwargs={'genre_name': 'fantasy'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to check the response data
    def test_search_books(self):
        # Test searching books without authentication
        response = self.client.get(reverse('search_books') + '?q=fantasy')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test searching books with authentication
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('search_books') + '?q=fantasy')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to check the response data
    def test_create_book(self):
        # Test creating a book without authentication
        data = {'title': 'Test Book', 'author': 'Test Author', 'synopsis': 'Test Synopsis', 'views': 0, 'rating': 0}
        response = self.client.post(reverse('create_book'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test creating a book with authentication
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('create_book'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add more assertions to check the response data
    
    
