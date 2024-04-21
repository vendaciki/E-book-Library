from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user}")
        super().save(*args, **kwargs)

