from django.views.generic import ListView, CreateView
from .models import Book
from .forms import PostBookForm


class BooksView(ListView):
    model = Book
    template_name = "knihy.html"
    ordering = ["-id"]


class AddBookView(CreateView):
    model = Book
    form_class = PostBookForm
    template_name = "pridat-knihu.html"
