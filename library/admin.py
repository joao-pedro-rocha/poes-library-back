from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'created_at',
                    'updated_at', 'is_active')
    list_display_links = ('title',)
    filter_horizontal = ('author',)
    readonly_fields = ('created_at', 'updated_at')
