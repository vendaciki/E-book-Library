from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Book, Author
from .forms import PostBookForm, PostAuthorForm
from django.urls import reverse_lazy


class BooksView(ListView):
    model = Book
    template_name = "knihy.html"
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        context['authors'] = authors

        return context

    def get_success_url(self):
            # Dynamically generate the success URL using self.object.id
            return reverse_lazy("detail-knihy", kwargs={'pk': self.object.id})
        # success_url = reverse_lazy("knihy")

class AddBookView(CreateView):
    model = Book
    form_class = PostBookForm
    template_name = "pridat-knihu.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "detail-knihy.html"


class UpdateBookDetail(UpdateView):
    model = Book
    form_class = PostBookForm
    template_name = "upravit-knihu.html"

    # def get_success_url(self):
    #     # Dynamically generate the success URL using self.object.id
    #     return reverse_lazy("detail-knihy", kwargs={'pk': self.object.id})
    # # success_url = reverse_lazy("knihy")


class SearchView(ListView):
    model = Book
    template_name = "vysledky-hledani.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Book.objects.filter(
            title__icontains=query
        )
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q")
        return context


class AddAuthorView(CreateView):
    model = Author 
    form_class = PostAuthorForm
    template_name = "pridat-autora.html"

    success_url = reverse_lazy("knihy")


class AuthorDetailView(DetailView):
    model = Author
    template_name = "detail-autora.html"
