from rest_framework import serializers
from .models import Book, Editorial, Author
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "firstname", "lastname", "birthdate"]
        extra_kwargs = {'books': {'required': False}}
        
class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ["id", "name"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description", "pub_date", "editorial"]
        
