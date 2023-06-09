from django.db import models
from django.contrib.auth.models import User


class Editorial(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    
class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    pub_date = models.DateField()
    editorial = models.ForeignKey(Editorial, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.editorial.name})"



    
class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
