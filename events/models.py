from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

event_choice=(
    ('Arangu',"Arangu"),
    ('Inter',"Inter")
    )

team_choice=(
    ('Single',"Single"),
    ('Group',"Group")
    )

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=10,choices=event_choice,blank=True)
    sg = models.CharField(max_length=10,choices=team_choice,blank=True,verbose_name="Single/Group")
    duration = models.CharField(max_length=50,blank=True, default='5mins')
    nop = models.IntegerField(default=1,verbose_name='Number of Participants', blank=True)
    slug = models.SlugField(max_length=200, blank=False, unique=True,default='slug')
    brief = models.CharField(max_length=400, blank=True)
    description = models.TextField()
    rules = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    date = models.CharField(max_length=50,blank=True)
    time = models.CharField(max_length=50,blank=True)
    venue = models.CharField(max_length=250,blank=True)
    url = models.URLField(default='url',verbose_name="Registration Link", blank=True)
    fees = models.IntegerField()
    prize = models.CharField(max_length=200)
    img = ProcessedImageField(upload_to="post_images",verbose_name='Image',blank=False)
    image_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(75, 40)], format='JPEG', options={'quality': 60})
    minreg = models.IntegerField(verbose_name='Minimum Registrations',default=15)
    
    #Meta
    #created_on = models.DateTimeField(auto_now_add=True, null=True)
    #updated_on = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
    	return self.name
#
   # def get_absolute_url(self):
  #      url = reverse('detailview', kwargs={'slug': self.slug})
   #     return url

   # def getname(self):
   #     return self.name





