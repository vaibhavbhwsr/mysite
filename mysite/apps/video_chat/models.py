from django.db import models

# Create your models here.


class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    record_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class MeetRecord(models.Model):
    channel = models.CharField(max_length=255)
    record_link = models.CharField(max_length=255, null=True, blank=True)
