from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")
    
    # přidávám class, se kterou pracuji v CSS; stejně tak můžu přidat jakýkoliv jiný parametr
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control shadow-sm"}),
            "author": forms.TextInput(attrs={"class": "form-control shadow-sm", "value": "", "id": "nick-name", "type": "hidden"}),
            # "author": forms.Select(attrs={"class": "form-control shadow-sm"}),
            "body": forms.Textarea(attrs={"class": "form-control shadow-sm"}),
        }

        labels = {
            "title": "Název",
            "author": "Autor",
            "body": "Obsah",
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }

        labels = {
            "title": "Název",
            "body": "Obsah"
        }