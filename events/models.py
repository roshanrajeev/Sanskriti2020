from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    fees = models.IntegerField()
    prize = models.CharField(max_length=200)
