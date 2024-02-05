from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# načte seznam článků
class HomeView(ListView):
    model = Post
    template_name = "index.html"
    # ordering = ["-id"]
    ordering = ["-post_date", "-id"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "detail-clanku.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "pridat-clanek.html"

# Pokud neimportuji PostForm z forms.py, tak pracuji se spodním class
# class AddPostView(CreateView):
#     model = Post
#     template_name = "pridat-clanek.html"
#     fields = "__all__"
#     # můžu definovat co se bude přidávat ve formulář:
#         # fields = ("title", "body")
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "upravit-clanek.html"
    # fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "smazat-clanek.html"
    success_url = reverse_lazy("home")
