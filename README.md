# REST API - A demo #

This is a small API REST for books, authors and editorials. This is just a demo, not ready for production.

### Requirements ###

This is written in Pyhton with Django and Django REST Framework. For the database we use a Sqlite one.

See **src/books/requirements.txt**.

### How to run it? ###


For running directly with Django:

	source ./src/bin/activate
	cd src/books/
	python3 manage.py runserver

You can also run it with docker:


### How to use it? ###

| Endpoint                                      | GET  | POST  | PUT  | DELETE  |
|:--|:--|:--|:--|:--|
| books/api/editorial                          | Lists all editorials. | Creates an editorial. | - | - |
| books/api/editorial/**\<int:editorial_id\>**         | Retrieves an editorial. | - | Updates an editorial. | Deletes an editorial. |
| books/api/editorial/**\<int:editorial_id\>**/books   | Retrieves all books published by an editorial. | - | - | - |
| books/api/author                             | Lists all authors. | Creates an author. | - | - |
| books/api/author/**\<int:author_id\>**               | Retrieves an author. | - | Updates an author. | Deletes an author. |
| books/api/author/**\<int:author_id\>**/books         | Retrieves all books written by an author. | - | - | - |
| books/api/author/**\<int:author_id\>**/book/**\<int:book_id\>** | - | - | Adds an author to the book's list of authors. | Deletes an author from the book's list of authors. |
| books/api/book                               | Lists all books. | Creates a book. | - | - |
| books/api/book/**\<int:book_id\>**                  | Retrieves a book. | -  | Updates a book. | Deletes a book. |
| books/api/book/**\<int:book_id\>**/authors          | Lists all authors for a given book. | - | - | - |

#### Example ####

We can get all books:

	http -a MY-USER:MY-PASSWORD GET http://127.0.0.1:8000/books/api/book

	HTTP/1.1 200 OK
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 300
	Content-Type: application/json
	Cross-Origin-Opener-Policy: same-origin
	Date: Fri, 09 Jun 2023 21:41:44 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.10.6
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY
	
	[
		{
			"description": "A description",
			"editorial": 2,
			"id": 1,
			"pub_date": "2022-09-12",
			"title": "A title"
		},
		{
			"description": "Another Description",
			"editorial": 3,
			"id": 2,
			"pub_date": "2022-09-12",
			"title": "A title 2"
		},
		{
			"description": "Yet another description",
			"editorial": 2,
			"id": 3,
			"pub_date": "2022-09-12",
			"title": "A title 3"
		}
	]

We can execute the same but POSTing instead of GETing. This should return an error:

	http -a MY-USER:MY-PASSWORD POST http://127.0.0.1:8000/books/api/book
	
	HTTP/1.1 400 Bad Request
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 174
	Content-Type: application/json
	Cross-Origin-Opener-Policy: same-origin
	Date: Fri, 09 Jun 2023 21:42:14 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.10.6
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY
	
	{
		"description": [
			"This field may not be null."
		],
		"editorial": [
			"This field may not be null."
		],
		"pub_date": [
			"This field may not be null."
		],
		"title": [
			"This field may not be null."
		]
	}

So we can send the data with the POST:

	echo '{"description": "A book desc", "editorial": 2, "pub_date": "2023-06-09", "title": "A book title"}' | http -a MY-USER:MY-PASSWORD POST http://127.0.0.1:8000/books/api/book
	
	HTTP/1.1 201 Created
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 97
	Content-Type: application/json
	Cross-Origin-Opener-Policy: same-origin
	Date: Fri, 09 Jun 2023 21:44:00 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.10.6
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY
	
	{
		"description": "A book desc",
		"editorial": 2,
		"id": 4,
		"pub_date": "2023-06-09",
		"title": "A book title"
	}

And we can DELETE the book just created:

	http -a MY-ADMIN:MY-PASSWORD DELETE http://127.0.0.1:8000/books/api/book/4
	
	HTTP/1.1 200 OK
	Allow: GET, PUT, DELETE, HEAD, OPTIONS
	Content-Length: 23
	Content-Type: application/json
	Cross-Origin-Opener-Policy: same-origin
	Date: Fri, 09 Jun 2023 21:49:19 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.10.6
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY
	
	{
		"res": "Book deleted!"
	}


