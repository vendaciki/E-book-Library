from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Book, Author, Genre
from .forms import PostBookForm, PostAuthorForm
from django.urls import reverse_lazy
from utils.google_books import get_review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


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
        # vypíše všechny žánry:
        # genres = Genre.objects.order_by("genre")
        
        # vypíše jen ty žánry, které mají knihy
        genres = Genre.objects.filter(book__isnull=False).distinct()
        context["genres"] = genres

        return context


class AddBookView(CreateView):
    model = Book
    form_class = PostBookForm
    template_name = "pridat-knihu.html"

    def get_success_url(self):
            # Dynamically generate the success URL using self.object.id
            return reverse_lazy("detail-knihy", kwargs={'slug': self.object.slug})
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
        return reverse_lazy("detail-knihy", kwargs={'slug': self.object.slug})
    # success_url = reverse_lazy("knihy")


class SearchView(ListView):
    model = Book
    template_name = "vysledky-hledani.html"

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     object_list = Book.objects.filter(
    #         title__icontains=query
    #     )
    #     return object_listclass SearchView(ListView):
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
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['query'] = self.request.GET.get("q")
    #     return context
    def get_queryset(self):
        query = self.request.GET.get("q")
        book_results = Book.objects.filter(
            title__icontains=query
        )
        author_results = Author.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return book_results, author_results
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        context["books"], context["authors"] = self.get_queryset()
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
    paginate_by = 35

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_books = self.get_queryset()

        # Use pagination
        paginator = Paginator(all_books, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context["all_books"] = paginator.page(page)
        except PageNotAnInteger:
            context["all_books"] = paginator.page(1)
        except EmptyPage:
            context["all_books"] = paginator.page(paginator.num_pages)

        return context


class AllAuthorsView(ListView):
    model = Author
    template_name = "vsichni-autori.html"
    paginate_by = 20

    def get_queryset(self):
        return Author.objects.order_by("last_name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_authors = self.get_queryset()

        # Use pagination
        paginator = Paginator(all_authors, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context["all_authors"] = paginator.page(page)
        except PageNotAnInteger:
            context["all_authors"] = paginator.page(1)
        except EmptyPage:
            context["all_authors"] = paginator.page(paginator.num_pages)

        return context


class AuthorsByCharView(ListView):
    template_name = "vsichni-autori-abecedne.html"
    context_object_name = 'filtered_authors'
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_char = self.kwargs.get("char")
        context["selected_char"] = selected_char
        return context

    def get_queryset(self):
        char = self.kwargs.get('char')
        return Author.objects.filter(last_name__istartswith=char).order_by('last_name')


class GenreDetailView(DetailView):
    model = Genre
    template_name = "zanr.html"
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve books for the specific genre
        context['books'] = Book.objects.filter(genre=self.object)

        return context