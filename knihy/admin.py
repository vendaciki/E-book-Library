from django.contrib import admin
from .models import Genre, Book, Author

# zpřístupní článek v Admin sekci
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
