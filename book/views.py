from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

# views.py control how the database model content is displayed


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    # List_view class by default sends a context variable called object_list to the template and we can access the list of objects in the template using this variable.
    # without overiding the context_object_name, the context variable will be either object_list or modelname_list, u can use one of them interchangably

    # or if u want to use a custom name for the context variable, you can override the context_object_name attribute. here we are using books as the context variable name
    context_object_name = 'books'
