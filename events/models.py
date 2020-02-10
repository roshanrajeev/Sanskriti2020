from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth import get_user_model
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
    event_type=models.CharField(max_length=10,choices=event_choice,blank=True)
    sg=models.CharField(max_length=10,choices=team_choice,blank=True,verbose_name="Single/Group")
    duration=models.CharField(max_length=50,default='5 min')
    nop=models.IntegerField(default=1,verbose_name='Number of Participants', blank=False)
    slug = models.SlugField(max_length=200)
    brief=models.CharField(max_length=400,blank=True)
    description = models.TextField()
    contact=models.CharField(max_length=30,blank=True)
    date=models.CharField(max_length=10,blank=True)
    time=models.CharField(max_length=10,blank=True)
    venue=models.CharField(max_length=250,blank=True)
    url = models.URLField(verbose_name="Registration Link")
    fees = models.IntegerField()
    prize = models.CharField(max_length=200)
    img=ProcessedImageField(upload_to="post_images",default='sans20.jpg',verbose_name='Thumbnail')
    image_thumbnail=ImageSpecField(source='img', processors=[ResizeToFill(75, 40)], format='JPEG', options={'quality': 60})
    minreg=models.IntegerField(verbose_name='Minimum Registrations',default=15)
    
    #Meta
    created_on=models.DateTimeField(auto_now_add=True, null=True   )
    added_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)

    #created_by=models.ForeignKey(User, related_name='Events',on_delete=models.CASCADE,auto_now_add=request.user.id )
    updated_on=models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
    	return self.name

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Event,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/events/%s/" % self.slug

    def getname(self):
        return self.name





