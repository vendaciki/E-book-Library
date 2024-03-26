from django.urls import path
from .views import UserRegisterView, UserEditView, UserLoginView, PasswordsChangeView, redirect_view
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registrace/", UserRegisterView.as_view(), name="registrace"),
    path("prihlaseni/", UserLoginView.as_view(), name="prihlaseni"),
    path("upravit-profil/", UserEditView.as_view(), name="upravit-profil"),
    path("password/", PasswordsChangeView.as_view(), name="password"),
    path("uspesne-zmeneno/", redirect_view, name="uspesne-zmeneno"),
  
]