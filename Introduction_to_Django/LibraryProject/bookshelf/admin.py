from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

#Custom adnim display
    search_fields = ('title', 'author')

#Enable search by title and author
    list_filter = ('publication_year')