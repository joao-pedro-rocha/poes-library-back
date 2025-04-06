from rest_framework import viewsets
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer
from library.models import Author,  Genre, Book


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        title_param = self.request.query_params.get('title')
        author_param = self.request.query_params.get('author')
        publication_param = self.request.query_params.get('publication')
        queryset = Book.objects.all()

        if title_param:
            queryset = queryset.filter(title__icontains=title_param)

        if author_param:
            if author_param.isnumeric():
                queryset = queryset.filter(author=author_param)
            else:
                queryset = queryset.filter(
                    author__name__icontains=author_param)

        if publication_param:
            queryset = queryset.filter(publication=publication_param)
        
        return queryset
