from django.contrib import admin
from django.urls import path
#from .views import EditorialListApiView, EditorialDetailApiView, AuthorListApiView, AuthorDetailApiView, BookListApiView, BookDetailApiView, EditorialBookListApiView
from .views import *


urlpatterns = [
    path('api/editorial', EditorialListApiView.as_view(), name="editorial-list"),
    path('api/editorial/<int:editorial_id>', EditorialDetailApiView.as_view(), name="editorial-detail"),
    path('api/editorial/<int:editorial_id>/books', EditorialBookListApiView.as_view(), name="editorial-book-list"),
    path('api/author', AuthorListApiView.as_view(), name="author-list"),
    path('api/author/<int:author_id>', AuthorDetailApiView.as_view(), name="author-detail"),
    path('api/author/<int:author_id>/books', AuthorBookListApiView.as_view(), name="author-book-list"),
    path('api/author/<int:author_id>/book/<int:book_id>', AuthorBookDetailApiView.as_view(), name="author-book-detail"),
    path('api/book', BookListApiView.as_view(), name="book-list"),
    path('api/book/<int:book_id>', BookDetailApiView.as_view(), name="book-detail"),
    path('api/book/<int:book_id>/authors', BookAuthorListApiView.as_view(), name="book-author-list"),
]
