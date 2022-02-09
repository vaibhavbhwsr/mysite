from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GroupChat(models.Model):
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE, related_name='group_chat'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-id']

    # returns group name
    def __str__(self):
        return self.name
