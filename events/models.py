from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='slug')
    description = models.TextField()
    url = models.URLField(default='url')
    fees = models.IntegerField()
    prize = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

    def get_url(self):
    	return self.url


