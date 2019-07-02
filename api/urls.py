from api.views import AuthorsView, BooksView
from django.urls import path

urlpatterns = [
    path('authors/', AuthorsView.as_view()),
    path('books/', BooksView.as_view()),
]