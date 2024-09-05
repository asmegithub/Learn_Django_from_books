from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from book.models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            author="William S. Vincent",
            publication_date="2020-01-01",
        )

    def test_api_listview(self):
        # This is to check the url name in the urls.py file
        response = self.client.get(reverse("book_list"))
        # This is to check if the response is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # This is to check if the book object is created
        self.assertEqual(Book.objects.count(), 1)
        # This is to check if the response contains the book object
        self.assertContains(response, self.book)
