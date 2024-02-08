from django.urls import path
from .views import BooksView, AddBookView, BookDetailView, UpdateBookDetail, SearchView, AddAuthorView

urlpatterns = [
    path("prehledknih/", BooksView.as_view(), name="knihy"),
    path("pridat-knihu/", AddBookView.as_view(), name="pridat-knihu"),
    path("detail-knihy/<int:pk>", BookDetailView.as_view(), name="detail-knihy"),
    path("upravit-knihu/<int:pk>", UpdateBookDetail.as_view(), name="upravit-knihu"),
    path("vysledky-hledani", SearchView.as_view(), name="vysledky-hledani"),
    path("pridat-autora", AddAuthorView.as_view(), name="pridat-autora"),
]

