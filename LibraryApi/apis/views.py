from django.shortcuts import render
from rest_framework import generics

from book.models import Book
from .serializers import BookSerializer


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    # This is to serialize the data in to json format to easily transefer the data over the network
    serializer_class = BookSerializer
