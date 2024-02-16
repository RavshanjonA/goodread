from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/book-list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    slug_url_kwarg = 'slug'
    template_name = "books/book-detail.html"
    context_object_name = "book"

