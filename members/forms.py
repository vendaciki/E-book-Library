from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput
from .models import Profile


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
    

    def clean(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"Tento email {email} už je zaregistrován.")
        return self.cleaned_data


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Uživatelské jméno', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Heslo", widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )

    class Meta:
        model = User
        fields = "__all__"
    
    # vycházím ze zdrojového kódu pro Django na Githubu
    error_messages = {
        "invalid_login": "Zadej správné uživatelské jméno a heslo. Pozor na velká a malá písmena."
     }


class AddonProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")
    
    def __init__(self, *args, **kwargs):
        super(AddonProfileForm, self).__init__(*args, **kwargs)

        self.fields["bio"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, required=False, label="Křestní jméno (volitelné)", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, required=False, label="Příjmení (volitelné)", widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=100, label="Přezdívka", widget=forms.TextInput(attrs={"class":"form-control readonly", "readonly":True}))
    # last_login = forms.CharField(max_length=100, label="Poslední přihlášení", widget=forms.TextInput(attrs={"class":"form-control", "disabled":True}))
    # is_superuser = forms.CharField(max_length=100, label="Superuživatel", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    # is_staff = forms.CharField(max_length=100, label="Personál", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    # is_active = forms.CharField(max_length=100, label="Je aktivní", widget=forms.CheckboxInput(attrs={"class":"form-check"}))
    date_joined = forms.CharField(max_length=100, label="Registrován od", widget=forms.TextInput(attrs={"class":"form-control readonly", "readonly":True})) 
    # password = forms.CharField(
    #     label="Heslo", 
    #     help_text=mark_safe("Hesla se neukládají přímo a tak je nelze zobrazit. <br /> Heslo můžeš změnit pomocí <a href='../password'>tohoto formuláře</a>."),
    #     widget=forms.TextInput(attrs={"class":"form-control readonly", "readonly":True})
    #     )


    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",  "date_joined")
    

    def __init__(self, *args, **kwargs):
        # Remove the password field from the form because it loads defaultly from inheriting from UserChangeForm
        super().__init__(*args, **kwargs)
        self.fields.pop('password')


    def clean_field(self, field_name):
        original_value = getattr(self.instance, field_name)
        new_value = self.cleaned_data[field_name]
        if original_value != new_value:
            raise forms.ValidationError(f"Změna tady není povolena.")
        return new_value


    def clean_username(self):
        return self.clean_field('username')

    # def clean_date_joined(self):
    #     return self.clean_field('date_joined')
    

class PasswordsChangeForm(PasswordChangeForm):
    # old_password = forms.CharField(
    #     label="Původní heslo",
    #     strip=False,
    #     widget=forms.PasswordInput(
    #         attrs={"class":"form-control", "autocomplete": "current-password", "autofocus": True}
    #     ),
    # )

    def __init__(self, *args, **kwargs):
        super(PasswordsChangeForm, self).__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs["class"] = "form-control"
        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs["class"] = "form-control"



class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))


#TODO toto nefunguje - nepridava class="form-control"

class ResetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs["class"] = "form-control"