from rest_framework import serializers
from library.models import Author, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorNameSerializer(many=True)
    genre = GenreNameSerializer()
    class Meta:
        model = Book
        fields = '__all__'
