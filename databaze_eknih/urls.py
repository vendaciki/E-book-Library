from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", HomeView.as_view(), name="clanky"),
    path("clanek/<int:pk>", ArticleDetailView.as_view(), name="detail-clanku"),
    path("pridatclanek/", AddPostView.as_view(), name="pridat-clanek"),
    path("clanek/upravit/<int:pk>", UpdatePostView.as_view(), name="upravit-clanek"),
    path("clanek/smazat/<int:pk>", DeletePostView.as_view(), name="smazat-clanek")
]