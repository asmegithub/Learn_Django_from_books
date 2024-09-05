# N.B App name  should be in plural form for simplicity


from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    # ISBN = models.CharField(max_length=13)

# The __str__ method is a special method that returns a string representation of the object.
# without this the admin interface will display the object as "Book object (1)"
#
    def __str__(self):
        return self.title
