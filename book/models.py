from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()

# The __str__ method is a special method that returns a string representation of the object.
# without this the admin interface will display the object as "Book object (1)"
#
    def __str__(self):
        return self.title + " by " + self.author + " on " + str(self.publication_date)
