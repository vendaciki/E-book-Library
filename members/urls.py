from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("registrace/", UserRegisterView.as_view(), name="registrace"),
  
]