from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
