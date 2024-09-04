from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book

# The CustomBookAdmin class is to customizes the admin interface for the Book model.


class CustomUserModel(UserAdmin):
    pass


class CustomBookAdmin(admin.ModelAdmin):
    # This will display the title, author, and publication date of each book in the admin interface.
    list_display = ('title', 'author', 'publication_date')
    # This will add a filter to the admin interface to filter books by publication date.
    list_filter = ('publication_date',)
    # This will add a search box to the admin interface and search books by title or author.
    search_fields = ('title', 'author')
    # This will order the books by publication date in descending order.
    ordering = ('-publication_date',)


admin.site.register(Book, CustomBookAdmin)
