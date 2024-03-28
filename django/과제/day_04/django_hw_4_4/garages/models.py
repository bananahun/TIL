from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200,null=True)
    capacity = models.IntegerField(null=True)
    is_parking_avaliable = models.BooleanField(null=True)
    opening_time = models.TimeField(null=True)
    closing_time = models.TimeField(null=True)