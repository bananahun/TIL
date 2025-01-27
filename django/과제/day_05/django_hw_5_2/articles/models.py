from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length = 20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)