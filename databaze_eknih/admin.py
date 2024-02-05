from django.contrib import admin
from .models import Post

# zpřístupní článek v Admin sekci
admin.site.register(Post)

