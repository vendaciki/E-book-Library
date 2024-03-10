from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, label="Křestní jméno (volitelné)", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, label="Příjmení (volitelné)", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, required=False, label="Křestní jméno (volitelné)", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, required=False, label="Příjmení (volitelné)", widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=100, label="Přezdívka", widget=forms.TextInput(attrs={"class":"form-control", "disabled":True}))
    # last_login = forms.CharField(max_length=100, label="Poslední přihlášení", widget=forms.TextInput(attrs={"class":"form-control", "disabled":True}))
    # is_superuser = forms.CharField(max_length=100, label="Superuživatel", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    # is_staff = forms.CharField(max_length=100, label="Personál", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    # is_active = forms.CharField(max_length=100, label="Je aktivní", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    date_joined = forms.CharField(max_length=100, label="Registrován od", widget=forms.TextInput(attrs={"class":"form-control", "disabled":True})) 
    password = forms.CharField(label="Heslo", widget=forms.TextInput(attrs={"class":"form-control", "disabled":True}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password", "date_joined")


