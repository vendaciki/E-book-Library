from django.contrib import admin
from .models import Genre, Book, Author, Publisher

# zpřístupní článek v Admin sekci
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
