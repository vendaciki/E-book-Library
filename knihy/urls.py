from django.urls import path
from .views import BooksView, AddBookView, BookDetailView, UpdateBookDetail, SearchView, AddAuthorView, AuthorDetailView, AllBooksView, AllAuthorsView, GenreDetailView

urlpatterns = [
    path("", BooksView.as_view(), name="knihy"),
    path("pridat-knihu/", AddBookView.as_view(), name="pridat-knihu"),
    path("detail-knihy/<int:pk>", BookDetailView.as_view(), name="detail-knihy"),
    path("upravit-knihu/<int:pk>", UpdateBookDetail.as_view(), name="upravit-knihu"),
    path("vysledky-hledani", SearchView.as_view(), name="vysledky-hledani"),
    path("pridat-autora", AddAuthorView.as_view(), name="pridat-autora"),
    path("detail-autora/<int:pk>", AuthorDetailView.as_view(), name="detail-autora"),
    path("vsechny-knihy/", AllBooksView.as_view(), name="vsechny-knihy"),
    path("vsichni-autori/", AllAuthorsView.as_view(), name="vsichni-autori"),
    path("zanr/<int:pk>", GenreDetailView.as_view(), name="zanr"),
]

