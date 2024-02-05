from django.urls import path
from .views import BooksView

urlpatterns = [
    path("prehledknih", BooksView.as_view(), name="knihy")
]

