from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Author
from .models import Post

admin.site.register(Author)
admin.site.register(Post)