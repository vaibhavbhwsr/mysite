from django.contrib import admin
from video_chat.models import RoomMember, MeetRecord

# Register your models here.

admin.site.register(RoomMember)
admin.site.register(MeetRecord)