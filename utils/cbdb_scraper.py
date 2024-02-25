from knihy.models import Book

for book in Book.objects.all():
    print(book)