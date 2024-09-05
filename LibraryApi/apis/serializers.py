from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date')
        # Alternatively, you could have used '__all__' to include all fields like: fields = '__all__'
