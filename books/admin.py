from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name', 'author_first_name',
                    'author_last_name', 'publish']


admin.site.register(Book, BookAdmin)
