from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    genre = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField()
    ISBN = models.CharField(max_length=13, unique=True)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    

    def __str__(self):
        return self.title

