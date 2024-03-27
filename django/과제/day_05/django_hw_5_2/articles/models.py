# from django.db import models

# Create your models here.

# articles/models.py

from django.db import models
from django.utils import timezone

class Article(models.Model):
    name = models.CharField(max_length=200)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

