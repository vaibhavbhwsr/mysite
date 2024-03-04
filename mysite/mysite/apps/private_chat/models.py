from django.contrib.auth import get_user_model
from django.db import models
from core.models import BaseModel

User = get_user_model()

# Create your models here.


class PrivateChat(BaseModel):
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(
        'OneOneGroup', on_delete=models.CASCADE, related_name='private_chat'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class OneOneGroup(BaseModel):
    name = models.CharField(max_length=255, unique=True, null=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_oog')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_oog')

    class Meta:
        ordering = ['-id']
        unique_together = [("user1", "user2"),]

    def save(self, *args, **kwargs):
        self.name = f"one-one-{'-'.join(sorted([str(self.user1.id), str(self.user2.id)]))}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
