from django.urls import path
from .views import BooksView, AddBookView

urlpatterns = [
    path("prehledknih/", BooksView.as_view(), name="knihy"),
    path("pridat-knihu/", AddBookView.as_view(), name="pridat-knihu")
]

