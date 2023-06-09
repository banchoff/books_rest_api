from django.shortcuts import render,  get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Book, Author, Editorial
from .serializers import BookSerializer, AuthorSerializer, EditorialSerializer

class EditorialListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwars):
        '''
        List all the Editorial items in the system
        '''
        editorials = Editorial.objects.all()
        serializer = EditorialSerializer(editorials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Creates an Editorial with given data
        '''
        data = {
            'name': request.data.get('name'), 
        }
        serializer = EditorialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditorialBookListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, editorial_id, *args, **kwars):
        '''
        List all Books published by editorial_id
        '''
        editorial = Editorial.objects.get(pk=editorial_id)
        books = editorial.book_set.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AuthorBookListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, author_id, *args, **kwars):
        '''
        List all Books published by author_id
        '''
        author = Author.objects.get(pk=author_id)
        books = author.books.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorBookDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, author_id, book_id, *args, **kwars):
        '''
        Makes author_id an author for book_id
        '''
        author = get_object_or_404(Author, pk=author_id)
        book = get_object_or_404(Book, pk=book_id)
        author.books.add(book)
        return Response(
            {"res": "Author-Book added!"},
            status=status.HTTP_200_OK
        )

    def delete(self, request, author_id, book_id, *args, **kwars):
        '''
        Deletes author_id from the list of authors of book_id
        '''
        author = get_object_or_404(Author, pk=author_id)
        book = get_object_or_404(Book, pk=book_id)
        author.books.remove(book)
        return Response(
            {"res": "Author-Book deleted!"},
            status=status.HTTP_200_OK
        )

class BookAuthorListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, book_id, *args, **kwars):
        '''
        List all Authors that published book_id
        '''
        book = Book.objects.get(pk=book_id)
        authors = book.author_set.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class AuthorListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwars):
        '''
        List all the Author items in the system
        '''
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Creates an Author with given data
        '''
        data = {
            'firstname': request.data.get('firstname'), 
            'lastname': request.data.get('lastname'), 
            'birthdate': request.data.get('birthdate'), 
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwars):
        '''
        List all the Book items in the system
        '''
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Creates a Book with given data
        '''
        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'pub_date': request.data.get('pub_date'), 
            'editorial': request.data.get('editorial'), 
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditorialDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, editorial_id, *args, **kwargs):
        '''
        Retrieves the Editorial with given editorial_id
        '''
        editorial = get_object_or_404(Editorial, pk=editorial_id)
        serializer = EditorialSerializer(editorial)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, editorial_id, *args, **kwargs):
        '''
        Updates the Editorial item with given editorial_id if exists
        '''
        editorial = get_object_or_404(Editorial, pk=editorial_id)
        data = {
            'name': request.data.get('name'), 
        }
        serializer = EditorialSerializer(instance = editorial, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, editorial_id, *args, **kwargs):
        '''
        Deletes the Editorial item with given editorial_id if exists
        '''
        editorial = get_object_or_404(Editorial, pk=editorial_id)
        editorial.delete()
        return Response(
            {"res": "Editorial deleted!"},
            status=status.HTTP_200_OK
        )

class AuthorDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, author_id, *args, **kwargs):
        '''
        Retrieves the Author with given author_id
        '''
        author = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, author_id, *args, **kwargs):
        '''
        Updates the Author item with given author_id if exists
        '''
        author = get_object_or_404(Author, pk=author_id)
        
        firstname  = request.data.get('firstname') if request.data.get('firstname') else author.firstname
        lastname   = request.data.get('lastname')  if request.data.get('lastname')  else author.lastname
        birthdate  = request.data.get('birthdate') if request.data.get('birthdate') else author.birthdate
        
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'birthdate': birthdate,
        }

        serializer = AuthorSerializer(instance = author, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, author_id, *args, **kwargs):
        '''        Deletes the Author item with given author_id if exists
        '''
        author = get_object_or_404(Author, pk=author_id)
        author.delete()
        return Response(
            {"res": "Author deleted!"},
            status=status.HTTP_200_OK
        )

class BookDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, book_id, *args, **kwargs):
        '''
        Retrieves the Book with given book_id
        '''
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, book_id, *args, **kwargs):
        '''
        Updates the Book item with given book_id if exists
        '''
        book = get_object_or_404(Book, pk=book_id)
        
        title       = request.data.get('title')       if request.data.get('title')        else book.title
        description = request.data.get('description') if request.data.get('description')  else book.description
        pub_date    = request.data.get('pub_date')    if request.data.get('pub_date')     else book.pub_date

        data = {
            'title': title,
            'description': description,
            'pub_date': pub_date,
        }

        serializer = BookSerializer(instance = book, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id, *args, **kwargs):
        '''
        Deletes the Book item with given book_id if exists
        '''
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response(
            {"res": "Book deleted!"},
            status=status.HTTP_200_OK
        )
