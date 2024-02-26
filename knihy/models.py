from django.db import models
from django.urls import reverse
from django.utils.text import slugify

"""
Po jakékoliv modifikaci kódu v tomto souboru je nutno provést migraci:
python manage.py makemigrations
python manage.py migrate
"""

class Author(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)
    

    class Meta:
        ordering = ["last_name"]


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False, db_index=True)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.genre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.genre)
        super().save(*args, **kwargs)
    

    class Meta:
        ordering = ["genre"]


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    publication_date = models.CharField(max_length=4)
    ISBN = models.CharField(max_length=17, unique=True)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    hodnoceni = models.IntegerField(null=True, blank=True, default=0)
    

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse("detail-knihy", args=(str(self.id))) 
    def get_absolute_url(self):
        return reverse("detail-knihy", args=self.slug) 

    # po dodatečném doprogramování slugu je potřeba jeho hodnotu vytvořit a to zavoláním fce save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)