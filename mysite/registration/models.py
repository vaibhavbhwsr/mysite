from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='images/post')
    tags = models.CharField(max_length=100, blank=True)
