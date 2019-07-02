from api.models import Book, Author
from rest_framework import serializers


class AuthorsSerializator(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('pk', 'name')

class BooksSerializator(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('pk', 'name', 'author')
