from django.contrib import admin
from django.urls import path
from .views import EditorialListApiView, EditorialDetailApiView, AuthorListApiView, AuthorDetailApiView, BookListApiView, BookDetailApiView

urlpatterns = [
    path('api/editorial', EditorialListApiView.as_view()),
    path('api/editorial/<int:editorial_id>', EditorialDetailApiView.as_view()),
    path('api/author', AuthorListApiView.as_view()),
    path('api/author/<int:author_id>', AuthorDetailApiView.as_view()),
    path('api/book', BookListApiView.as_view()),
    path('api/book/<int:book_id>', BookDetailApiView.as_view()),
]
