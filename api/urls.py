from api.views import AuthorsView, BooksView, BookDetailView
from django.urls import path

urlpatterns = [
    path('authors/', AuthorsView.as_view()),
    path('books/', BooksView.as_view()),
    path('books/<int:book_id>/', BookDetailView.as_view()),
]