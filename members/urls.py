from django.urls import path
from .views import UserRegisterView, UserEditView, UserLoginView

urlpatterns = [
    path("registrace/", UserRegisterView.as_view(), name="registrace"),
    path("prihlaseni/", UserLoginView.as_view(), name="prihlaseni"),
    path("upravit-profil/", UserEditView.as_view(), name="upravit-profil"),
  
]