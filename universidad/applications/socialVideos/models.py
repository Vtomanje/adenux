from django.db import models
from django.contrib.auth.models import User
# apps terceros
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.


class SocialVideo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts/images", default="default.jpg", blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    


