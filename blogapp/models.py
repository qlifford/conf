from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=350)
    # slug = models.SlugField()
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' +  str(self.author)

    def get_absolute_url(self):
        # return reverse('blog-detail', args=str(self.id))
        return reverse('home-page')