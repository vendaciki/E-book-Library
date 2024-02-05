from django.views.generic import ListView
from .models import Book


class BooksView(ListView):
    model = Book
    template_name = "knihy.html"
    ordering = ["-id"]
