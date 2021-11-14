from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # This is how we can registered our Post/AnyOther model from models.py
    list_display = ('description', 'user_name', 'date_posted')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'post', 'user')
