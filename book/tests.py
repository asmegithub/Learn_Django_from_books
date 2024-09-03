from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            author="Tom Christie",
            publication_date="2021-01-01",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.publication_date, "2021-01-01")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tom Christie")
        self.assertTemplateUsed(response, "books/book_list.html")
