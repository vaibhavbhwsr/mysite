# Generating tokens every time using signals for new user copied from drf.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa: F401
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):   # Could not able to change model-name here because migration from User to Custom User
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
