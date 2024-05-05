from django import forms
from .models import Book, Author, Genre
from django.core.exceptions import ValidationError



class PostBookForm(forms.ModelForm):
    # genre1 = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    # genre2 = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    # genre3 = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, empty_label="", widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))
    
    
    author_search = forms.CharField(label='Autor', widget=forms.TextInput(attrs={"class": "form-control shadow-sm", "placeholder": "Zadej příjmení..."}))
    # epub_file = forms.ClearableFileInput(attrs={'class': 'form-control-file'})

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Check if the user is an admin
        if not (self.request and self.request.user.is_staff):
            # If not an admin, hide the epub_file field
            self.fields['epub_file'].widget = forms.HiddenInput()

    class Meta:
        model = Book
        fields = ("title", "author_search", "author", "genre", "publication_date", "ISBN", "summary", "cover_image", "epub_file")
    
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
                'epub_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
            }
        
        labels = {
            'title': 'Název',
            'genre': 'Žánr',
            'publication_date': 'Rok vydání',
            'ISBN': 'ISBN',
            'summary': 'Souhrn',
            'cover_image': 'Obrázek obalu',
            'epub_file': 'E-kniha v EPUB formátu',
        }
    

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
    
    def clean_first_name(self):
        # Capitalize the first letter of the first name
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        # Capitalize the first letter of the last name
        return self.cleaned_data['last_name'].capitalize()