from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import Book, Author, Genre
from .forms import PostBookForm, PostAuthorForm
from django.urls import reverse_lazy
from utils.google_books import get_review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Pass the request object to the form
        return kwargs

    def get_success_url(self):
        # Dynamically generate the success URL using self.object.id
        return reverse_lazy("detail-knihy", kwargs={'slug': self.object.slug})
        # success_url = reverse_lazy("knihy")
    

class AuthorAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        qs = Author.objects.filter(last_name__istartswith=query)[:20]
        authors = [{'id': author.id, 'label': f"{author.last_name} {author.first_name}", "value": f"{author.last_name} {author.first_name}"} for author in qs]
        return JsonResponse(authors, safe=False)


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


class DownloadEpubView(View):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        original_file_name = book.epub_file.name
        response = HttpResponse(book.epub_file.read(), content_type='application/epub+zip')
        response['Content-Disposition'] = f'attachment; filename={original_file_name}'
        return response

    

class UpdateBookDetail(UpdateView):
    model = Book
    form_class = PostBookForm
    template_name = "upravit-knihu.html"

    # opravňuje admina k editaci PostBookForm pro epub
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Pass the request object to the form
        return kwargs

    def get_success_url(self):
        # Dynamically generate the success URL using self.object.id
        return reverse_lazy("detail-knihy", kwargs={'slug': self.object.slug})
    # success_url = reverse_lazy("knihy")

    def get_initial(self):
        # Set initial values for the form
        initial = super().get_initial()
        author = self.object.author
        # Concatenate first_name and last_name for author_search
        initial['author_search'] = f"{author.first_name} {author.last_name}"
        # Add other initial values if needed
        return initial


class DeleteBookDetailView(DeleteView):
    model = Book
    template_name = "smazat-knihu.html"
    success_url = reverse_lazy("home")


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
        # author_results = Author.objects.filter(
        #         Q(first_name__icontains=query) | Q(last_name__icontains=query)
        #     )
        if " " in query and len(query.split()) > 1:
            try:
                author_results = Author.objects.filter(
                    Q(first_name__icontains=query) | Q(last_name__icontains=query) | 
                    Q(first_name__icontains=query.split()[0], last_name__icontains=query.split()[1]) | 
                    Q(first_name__icontains=query.split()[1], last_name__icontains=query.split()[0])
                )
            except (IndexError, UnboundLocalError):
                pass
        else:
            query = query.strip()
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

    success_url = reverse_lazy("home")

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        existing_author = Author.objects.filter(first_name=first_name, last_name=last_name).first()

        if existing_author:
            return render(self.request, self.template_name, {'form': form, 'error_message': 'Autor už existuje.'})
        else:
            return super().form_valid(form)


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


class BooksByCharView(ListView):
    template_name = "vsechny-knihy-abecedne.html"
    context_object_name = "filtered_books"
    model = Book
    paginate_by = 35

    def get_queryset(self):
        char = self.kwargs.get("char")
        return Book.objects.filter(title__istartswith=char).order_by("title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_char = self.kwargs.get("char")
        context["selected_char"] = selected_char
        filtered_books = self.get_queryset()

        # Use pagination
        paginator = Paginator(filtered_books, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context["all_books"] = paginator.page(page)
        except PageNotAnInteger:
            context["all_books"] = paginator.page(1)
        except EmptyPage:
            context["all_books"] = paginator.page(paginator.num_pages)

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