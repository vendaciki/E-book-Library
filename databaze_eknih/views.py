from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# načte seznam článků
class HomeView(ListView):
    model = Post
    template_name = "index.html"
    # ordering = ["-id"]
    ordering = ["-post_date", "-id"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "detail-clanku.html"


class AddPostView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = "pridat-clanek.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Pokud neimportuji PostForm z forms.py, tak pracuji se spodním class
# class AddPostView(CreateView):
#     model = Post
#     template_name = "pridat-clanek.html"
#     fields = "__all__"
#     # můžu definovat co se bude přidávat ve formulář:
#         # fields = ("title", "body")
    
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "upravit-clanek.html"
    # fields = ["title", "body"]

   # kontroluje, že editor článku je autor nebo admin
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "smazat-clanek.html"
    success_url = reverse_lazy("clanky")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff
