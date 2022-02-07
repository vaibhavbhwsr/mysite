from django.contrib import admin
from group_chat.models import GroupChat, Group

# Register your models here.


@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'timestamp', 'group']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
