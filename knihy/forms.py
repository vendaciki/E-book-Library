from django import forms
from .models import Book, Author, Genre
from django.core.exceptions import ValidationError



class PostBookForm(forms.ModelForm):
    # genre1 = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    # genre2 = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    # genre3 = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    
    
    author_search = forms.CharField(label='Autor', widget=forms.TextInput(attrs={"class": "form-control shadow-sm", "placeholder": "Zadej příjmení..."}))

    class Meta:
        model = Book
        fields = ("title", "author_search", "author", "genre", "publication_date", "ISBN", "summary", "cover_image")
    
    # přidávám class, se kterou pracuji v CSS; stejně tak můžu přidat jakýkoliv jiný parametr
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control shadow-sm'}),
                'author': forms.HiddenInput(),
                # 'genre': forms.Select(attrs={'class': 'form-control shadow-sm'}),
                'genre': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
                # 'genre': forms.SelectMultiple(),
                'publication_date': forms.DateInput(attrs={'class': 'form-control datepicker shadow-sm'}),
                'ISBN': forms.TextInput(attrs={'class': 'form-control shadow-sm'}),
                'summary': forms.Textarea(attrs={'class': 'form-control shadow-sm', 'rows': 4}),
                'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        
        labels = {
            'title': 'Název',
            'genre': 'Žánr',
            'publication_date': 'Datum vydání',
            'ISBN': 'ISBN',
            'summary': 'Souhrn',
            'cover_image': 'Obrázek obalu',
        }
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     genre1 = cleaned_data.get('genre1')
    #     genre2 = cleaned_data.get('genre2')
    #     genre3 = cleaned_data.get('genre3')

    #     # Ensure genre1 is selected
    #     if not genre1:
    #         raise ValidationError({'genre1': 'This field is required.'})

    #     return cleaned_data





class PostAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name")

    # přidávám class, se kterou pracuji v CSS; stejně tak můžu přidat jakýkoliv jiný parametr
        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control shadow-sm'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control shadow-sm'}),
            }
        
        labels = {
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
        }