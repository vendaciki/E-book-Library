from django import forms
from .models import Book

class PostBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
    
    # přidávám class, se kterou pracuji v CSS; stejně tak můžu přidat jakýkoliv jiný parametr
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'genre': forms.Select(attrs={'class': 'form-control'}),
                'publication_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
                'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
                'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        
        labels = {
            'title': 'Název',
            'author': 'Autor',
            'genre': 'Žánr',
            'publication_date': 'Datum vydání',
            'ISBN': 'ISBN',
            'summary': 'Souhrn',
            'cover_image': 'Obrázek obalu',
        }