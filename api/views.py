from django.shortcuts import render
from api.models import Author, Book
from api.serializers import AuthorsSerializator, BooksSerializator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class AuthorsView(APIView):
    serializer_class = AuthorsSerializator

    # list of authors + count
    def get(self, request, format=None):

        all_authors = Author.objects.all()
        serializator = AuthorsSerializator(all_authors, many=True)

        data = list()
        data.append({'count': all_authors.count()})
        data.extend(serializator.data)

        return Response(data)


    def post(self, request, format=None):
        serializator = AuthorsSerializator(data=request.data)
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data, status=status.HTTP_201_CREATED)
        return Response(serializator.errors, status=status.HTTP_400_BAD_REQUEST)



class BooksView(APIView):
    serializer_class = BooksSerializator

    # list of books + count
    def get(self, request, format=None):
        all_books = Book.objects.all()
        serializator = BooksSerializator(all_books, many=True)

        data = list()
        data.append({'count': all_books.count()})
        data.extend(serializator.data)

        return Response(data)

    def post(self, request, format=None):
        serializator = BooksSerializator(data=request.data)
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data, status=status.HTTP_201_CREATED)
        return Response(serializator.errors, status=status.HTTP_400_BAD_REQUEST)