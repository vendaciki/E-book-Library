def books_count(request):
    from knihy.models import Book
    return {"books_count": Book.objects.count()}