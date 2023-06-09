from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from .models import *
import json

class BookTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
    
    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial test")
        url = reverse('book-list')
        data = {"title": "Test Book Title",
                "description": "Test Book Description",
                "pub_date": "2023-06-09",
                "editorial": editorial.id
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book Title')
        self.client.logout()

    def test_create_book_non_existent_editorial(self):
        """
        Ensure we cannot create a new book object if the editorial does not exist.
        """
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial test")
        url = reverse('book-list')
        data = {"title": "Test Book Title",
                "description": "Test Book Description",
                "pub_date": "2023-06-09",
                "editorial": editorial.id+1
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.count(), 0)
        self.client.logout()
        
    def test_list_book(self):
        """
        Ensure we can list all Book objects.
        """
        editorial = Editorial.objects.create(name="Editorial test")
        Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        Book.objects.create(title="Book Testing 2", description="Description 2", pub_date="2023-06-09", editorial=editorial)
        
        self.client.login(username='testuser', password='testing')

        url = reverse('book-list')
        data = {}
        response = self.client.get(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], 'Book Testing 1')
        self.assertEqual(response.data[1]["title"], 'Book Testing 2')
        self.client.logout()

    def test_delete_book(self):
        """
        Ensure we can delete a Book object.
        """        
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        
        url = reverse('book-detail', kwargs={'book_id': book.id})
        data = {}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.client.logout()

    def test_delete_non_existent_book(self):
        """
        Ensure we cannot delete a non-existen Book object.
        """        
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        
        url = reverse('book-detail', kwargs={'book_id': book.id+1})
        data = {}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Book.objects.count(), 1)
        self.client.logout()
        
    def test_change_book_title(self):
        """
        Ensure we can change a Book object.
        """
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
                
        url = reverse('book-detail', kwargs={'book_id': book.id})
        data = {"title": "Book Testing 2"}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Book Testing 2')
        self.client.logout()
                
        
class EditorialTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
    
    def test_create_editorial(self):
        """
        Ensure we can create a new editorial object.
        """
        self.client.login(username='testuser', password='testing')

        url = reverse('editorial-list')
        data = {"name": "Test Editorial"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Editorial.objects.count(), 1)
        self.assertEqual(Editorial.objects.get().name, 'Test Editorial')
        self.client.logout()

    def test_list_editorial(self):
        """
        Ensure we can list all Editorial objects.
        """

        Editorial.objects.create(name="Editorial Testing 1")
        Editorial.objects.create(name="Editorial Testing 2")
        
        self.client.login(username='testuser', password='testing')

        url = reverse('editorial-list')
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], 'Editorial Testing 1')
        self.assertEqual(response.data[1]["name"], 'Editorial Testing 2')
        self.client.logout()

    def test_delete_editorial(self):
        """
        Ensure we can delete an Editorial object.
        """        
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        url = reverse('editorial-detail', kwargs={'editorial_id': editorial.id})
        data = {}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Editorial.objects.count(), 0)
        self.client.logout()

    def test_change_editorial_name(self):
        """
        Ensure we can change an Editorial object.
        """
        self.client.login(username='testuser', password='testing')
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        url = reverse('editorial-detail', kwargs={'editorial_id': editorial.id})
        data = {"name": "Editorial Testing 2"}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Editorial.objects.count(), 1)
        self.assertEqual(Editorial.objects.get().name, 'Editorial Testing 2')
        self.client.logout()
        
class AuthorTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
    
    def test_create_author(self):
        """
        Ensure we can create a new author object.
        """
        self.client.login(username='testuser', password='testing')
        url = reverse('author-list')
        data = {"firstname": "Test Author Firstname",
                "lastname": "Test Author Lastname",
                "birthdate": "1981-12-02"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().firstname, 'Test Author Firstname')
        self.client.logout()

    def test_list_author(self):
        """
        Ensure we can list all Author objects.
        """
        Author.objects.create(firstname="Firstname 1", lastname="lastname", birthdate="1981-12-02")
        Author.objects.create(firstname="Firstname 2", lastname="lastname", birthdate="1981-12-02")
        
        self.client.login(username='testuser', password='testing')

        url = reverse('author-list')
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["firstname"], 'Firstname 1')
        self.assertEqual(response.data[1]["firstname"], 'Firstname 2')
        self.client.logout()

    def test_delete_author(self):
        """
        Ensure we can delete an Author object.
        """        
        self.client.login(username='testuser', password='testing')
        author = Author.objects.create(firstname="Firstname", lastname="lastname", birthdate="1981-12-02")
        
        url = reverse('author-detail', kwargs={'author_id': author.id})
        data = {}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), 0)
        self.client.logout()

    def test_change_author_firstname(self):
        """
        Ensure we can change an Author object.
        """
        self.client.login(username='testuser', password='testing')
        author = Author.objects.create(firstname="Firstname", lastname="lastname", birthdate="1981-12-02")
                
        url = reverse('author-detail', kwargs={'author_id': author.id})
        data = {"firstname": "Firstname 2"}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().firstname, 'Firstname 2')
        self.client.logout()
        

class AuthorBookTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
    
    def test_add_author_to_book(self):
        """
        Ensure we can add an author_id to the given book_id's list of authors.
        """
        self.client.login(username='testuser', password='testing')

        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        author = Author.objects.create(firstname="Firstname", lastname="lastname", birthdate="1981-12-02")


        url = reverse('author-book-detail', kwargs={'author_id': author.id, 'book_id': book.id})
        data = {}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.books.count(), 1)
        self.assertEqual(book.author_set.count(), 1)
        self.client.logout()

    def test_delete_author_from_book(self):
        """
        Ensure we can delete author_id from book_id's list of authors.
        """
        self.client.login(username='testuser', password='testing')

        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        author = Author.objects.create(firstname="Firstname", lastname="lastname", birthdate="1981-12-02")
        author.books.add(book)

        url = reverse('author-book-detail', kwargs={'author_id': author.id, 'book_id': book.id})
        data = {}
        response = self.client.delete(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.books.count(), 0)
        self.assertEqual(book.author_set.count(), 0)
        self.client.logout()

    def test_list_authors_for_book(self):
        """
        Ensure we can list all Authors for the given book_id.
        """
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        author1 = Author.objects.create(firstname="Firstname 1", lastname="lastname 1", birthdate="1981-12-02")
        author2 = Author.objects.create(firstname="Firstname 2", lastname="lastname 2", birthdate="1981-12-02")
        author1.books.add(book)
        author2.books.add(book)
        
        self.client.login(username='testuser', password='testing')

        url = reverse('book-author-list', kwargs={'book_id': book.id})
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["firstname"], 'Firstname 1')
        self.assertEqual(response.data[1]["firstname"], 'Firstname 2')
        self.client.logout()

   
    def test_list_books_for_author(self):
        """
        Ensure we can list all Books for the given author_id.
        """
        editorial = Editorial.objects.create(name="Editorial Testing 1")
        book1 = Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        book2 = Book.objects.create(title="Book Testing 2", description="Description 2", pub_date="2023-06-09", editorial=editorial)
        author = Author.objects.create(firstname="Firstname 1", lastname="lastname 1", birthdate="1981-12-02")
        author.books.add(book1)
        author.books.add(book2)
        
        self.client.login(username='testuser', password='testing')

        url = reverse('author-book-list', kwargs={'author_id': author.id})
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], 'Book Testing 1')
        self.assertEqual(response.data[1]["title"], 'Book Testing 2')
        self.client.logout()
     


class EditorialBookTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
    
    def test_list_books_for_editorial(self):
        """
        Ensure we can list all books for editorial_id.
        """
        self.client.login(username='testuser', password='testing')

        editorial = Editorial.objects.create(name="Editorial Testing 1")
        Book.objects.create(title="Book Testing 1", description="Description 1", pub_date="2023-06-09", editorial=editorial)
        Book.objects.create(title="Book Testing 2", description="Description 2", pub_date="2023-06-09", editorial=editorial)

        url = reverse('editorial-book-list', kwargs={'editorial_id': editorial.id})
        data = {}
        response = self.client.get(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], 'Book Testing 1')
        self.assertEqual(response.data[1]["title"], 'Book Testing 2')
        self.client.logout()
