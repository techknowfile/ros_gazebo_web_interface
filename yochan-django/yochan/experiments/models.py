from django.db import models

# Create your models here.
class GazeboVideoStream(models.Model):
    video_url = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
 
    
