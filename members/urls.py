from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path("registrace/", UserRegisterView.as_view(), name="registrace"),
    path("upravit-profil/", UserEditView.as_view(), name="upravit-profil"),
  
]