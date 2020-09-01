from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to = '')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title