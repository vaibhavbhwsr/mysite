from django.contrib import admin

from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # This is how we can registered our Post/AnyOther model from models.py
    list_display = ('description', 'user_name', 'date_posted')
