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

class AuthorListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwars):
        '''
        List all the Author items in the system
        '''
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwars):
        '''
        List all the Book items in the system
        '''
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditorialDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, editorial_id, *args, **kwargs):
        '''
        Retrieves the Editorial with given editorial_id
        '''
        editorial = get_object_or_404(Editorial, pk=editorial_id)
        serializer = EditorialSerializer(editorial)
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

    def put(self, request, author_id, *args, **kwargs):
        '''
        Updates the Author item with given author_id if exists
        '''
        author = get_object_or_404(Author, pk=author_id)
        data = {
            'firstname': request.data.get('firstname'), 
            'lastname': request.data.get('lastname'), 
            'birthdate': request.data.get('birthdate'), 
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

    def put(self, request, book_id, *args, **kwargs):
        '''
        Updates the Book item with given book_id if exists
        '''
        book = get_object_or_404(Author, pk=book_id)
        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'pub_year': request.data.get('pub_year'), 
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


    # https://blog.logrocket.com/django-rest-framework-create-api/
    # https://kingsleytorlowei.medium.com/building-a-many-to-many-modelled-rest-api-with-django-rest-framework-d41f54fe372
# class AuthorBookDetailApiView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, author_id, *args, **kwargs):
#         '''
#         Retrieves all the books written by an author_id
#         '''
#         author = get_object_or_404(Author, pk=author_id)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         '''
#         Assigns Creates an Author with given data
#         '''
#         data = {
#             'firstname': request.data.get('firstname'), 
#             'lastname': request.data.get('lastname'), 
#             'birthdate': request.data.get('birthdate'), 
#         }
#         serializer = AuthorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, author_id, *args, **kwargs):
#         '''
#         Updates the Author item with given author_id if exists
#         '''
#         author = get_object_or_404(Author, pk=author_id)
#         data = {
#             'firstname': request.data.get('firstname'), 
#             'lastname': request.data.get('lastname'), 
#             'birthdate': request.data.get('birthdate'), 
#         }
#         serializer = AuthorSerializer(instance = author, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, author_id, *args, **kwargs):
#         '''        Deletes the Author item with given author_id if exists
#         '''
#         author = get_object_or_404(Author, pk=author_id)
#         author.delete()
#         return Response(
#             {"res": "Author deleted!"},
#             status=status.HTTP_200_OK
#         )
