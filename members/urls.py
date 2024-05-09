from django.urls import path
from .views import UserRegisterView, UserEditView, UserLoginView, PasswordsChangeView, redirect_view, ShowUserProfileView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registrace/", UserRegisterView.as_view(), name="registrace"),
    path("prihlaseni/", UserLoginView.as_view(), name="prihlaseni"),
    path("upravit-profil/", UserEditView.as_view(), name="upravit-profil"),
    path("password/", PasswordsChangeView.as_view(), name="password"),
    path('obnovit-heslo/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('obnovit-heslo/hotovo/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/hotovo/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("uspesne-zmeneno/", redirect_view, name="uspesne-zmeneno"),
    path("uzivatel-<slug:slug>/", ShowUserProfileView.as_view(), name="profil")
  
]