from django.contrib.auth.models import User
from django.db import models
from core.models import BaseModel

# Create your models here.


class GroupChat(BaseModel):
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE, related_name='group_chat'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Group(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
