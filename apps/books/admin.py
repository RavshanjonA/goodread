from django.contrib import admin

from apps.books.models import Book, BookAuthor, BookReview, BookGenre

admin.site.register([ BookAuthor, BookReview, BookGenre])


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ["title"]
    }
