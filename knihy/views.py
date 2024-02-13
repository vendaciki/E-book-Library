from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Book, Author, Genre
from .forms import PostBookForm, PostAuthorForm
from django.urls import reverse_lazy
from utils.google_books import get_review


class BooksView(ListView):
    model = Book
    template_name = "knihy.html"
    ordering = ["-id"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # authors = Author.objects.all()
        last_8_authors = Author.objects.order_by("-id")[:8]
        context["authors"] = last_8_authors

        genres = Genre.objects.order_by("genre")
        context["genres"] = genres

        return context


class AddBookView(CreateView):
    model = Book
    form_class = PostBookForm
    template_name = "pridat-knihu.html"

    def get_success_url(self):
            # Dynamically generate the success URL using self.object.id
            return reverse_lazy("detail-knihy", kwargs={'pk': self.object.id})
        # success_url = reverse_lazy("knihy")

class BookDetailView(DetailView):
    model = Book
    template_name = "detail-knihy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch reviews using the utility function
        average_rating, ratings_count = get_review(self.object.title, "AIzaSyA36DPoAS-veBCYv-gvPvuwuXsn4CfTyUI")
        

        # Add review data to the context
        context['average_rating'] = average_rating
        context['ratings_count'] = ratings_count
        print(average_rating)
        return context
    

class UpdateBookDetail(UpdateView):
    model = Book
    form_class = PostBookForm
    template_name = "upravit-knihu.html"

    def get_success_url(self):
        # Dynamically generate the success URL using self.object.id
        return reverse_lazy("detail-knihy", kwargs={'pk': self.object.id})
    # success_url = reverse_lazy("knihy")


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


class AllBooksView(ListView):
    model = Book
    template_name = "vsechny-knihy.html"
    ordering = ["title"]


class AllAuthorsView(ListView):
    model = Author
    template_name = "vsichni-autori.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_authors = Author.objects.order_by("last_name")
        context["all_authors"] = all_authors
        return context


class GenreDetailView(DetailView):
    model = Genre
    template_name = "zanr.html"
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve books for the specific genre
        context['books'] = Book.objects.filter(genre=self.object)

        return context