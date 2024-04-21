from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, LoginForm, PasswordsChangeForm, AddonProfileForm
from .models import Profile


def redirect_view(request):
    return render(request, "registration/uspesne-zmeneno.html")


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registrace.html"
    success_url = reverse_lazy("prihlaseni")


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "registration/prihlaseni.html"
    success_url = reverse_lazy("home")


class UserEditView(generic.UpdateView):
    # form_class = EditProfileForm
    template_name = "registration/upravit-profil.html"
    success_url = reverse_lazy("uspesne-zmeneno")

    def get(self, request, *args, **kwargs):
        addons_form = AddonProfileForm(instance=request.user.profile)
        edit_form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'addons_form': addons_form, 'edit_form': edit_form})

    def post(self, request, *args, **kwargs):
        addons_form = AddonProfileForm(request.POST, instance=request.user.profile)
        edit_form = EditProfileForm(request.POST, instance=request.user)
        if addons_form.is_valid() and edit_form.is_valid():
            addons_form.save()
            edit_form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'addons_form': addons_form, 'edit_form': edit_form})



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = "registration/zmenit-heslo.html"
    success_url = reverse_lazy("uspesne-zmeneno")


class ShowUserProfileView(DetailView):
    model = Profile
    template_name = "profil.html"
    success_url = reverse_lazy("profil")