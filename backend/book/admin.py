from django.contrib import admin
from .models import BookModel


@admin.register(BookModel)
class Book(admin.ModelAdmin):
    list_display = ('name', 'author', 'pages', 'publish')
    list_filter = ('author', 'name')
