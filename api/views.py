from django.shortcuts import render
from django.http import HttpResponse
from api.models import Author, Book
from api.serializers import AuthorsSerializator, BooksSerializator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class AuthorsView(APIView):
    serializer_class = AuthorsSerializator

    # list of authors + count
    def get(self, request):

        all_authors = Author.objects.all()
        serializator = AuthorsSerializator(all_authors, many=True)

        data = list()
        data.append({'count': all_authors.count()})
        data.extend(serializator.data)

        return Response(data)

    # create new author
    def post(self, request):
        serializator = AuthorsSerializator(data=request.data)
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data, status=status.HTTP_201_CREATED)
        return Response(serializator.errors, status=status.HTTP_400_BAD_REQUEST)



class BooksView(APIView):
    serializer_class = BooksSerializator

    # list of books + count
    def get(self, request):
        all_books = Book.objects.all()
        serializator = BooksSerializator(all_books, many=True)

        data = list()
        data.append({'count': all_books.count()})
        data.extend(serializator.data)

        return Response(data)

    # create new book
    def post(self, request):
        serializator = BooksSerializator(data=request.data)
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data, status=status.HTTP_201_CREATED)
        return Response(serializator.errors, status=status.HTTP_400_BAD_REQUEST)



class BookDetailView(APIView):
    serializer_class = BooksSerializator

    def get_book(self, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return HttpResponse(status=404)


    # get book info by id
    def get(self, request, book_id):

        book = self.get_book(book_id)
        serializator = BooksSerializator(book)
        return Response(serializator.data)



    # update book by id
    def put(self, request, book_id):

        book = self.get_book(book_id)
        serializator = BooksSerializator(book, data=request.data)
        if serializator.is_valid():
            serializator.save()
            return Response(serializator.data)
        return Response(serializator.errors, status=status.HTTP_400_BAD_REQUEST)


    # delete book by id
    def delete(self, request, book_id):
        book = self.get_book(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)