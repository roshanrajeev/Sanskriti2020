from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
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
    nop=models.CharField(max_length=10,choices=team_choice,blank=True,verbose_name="Single/Group")
    slug = models.SlugField(max_length=200, default='slug')
    brief=models.CharField(max_length=400,blank=True)
    description = models.TextField()
    contact=models.CharField(max_length=30,blank=True)
    date=models.CharField(max_length=10,blank=True)
    time=models.CharField(max_length=10,blank=True)
    venue=models.CharField(max_length=250,blank=True)
    url = models.URLField(default='url',verbose_name="Registration Link")
    fees = models.IntegerField()
    prize = models.CharField(max_length=200)
    image=ProcessedImageField(upload_to="post_images",default='White_full.jpg',verbose_name='Thumbnail')
    image_thumbnail=ImageSpecField(source='image', processors=[ResizeToFill(75, 40)], format='JPEG', options={'quality': 60})
    minreg=models.IntegerField(verbose_name='Minimum Registrations',default=10)
    #Meta
    created_on=models.DateTimeField(auto_now_add=True, null=True   )
    #created_by=models.ForeignKey(User, related_name='Events',on_delete=models.CASCADE, null=True, )
    updated_on=models.DateTimeField(null=True, auto_now_add=True)

    def save_event(self, request, obj, form, change):
        if not obj.pk:
        # Only set added_by during the first save.
            obj.created_by = request.user
        super().save_event(request, obj, form, change)

    def __str__(self):
    	return self.name

    def get_url(self):
    	return self.url


