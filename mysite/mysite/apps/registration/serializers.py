from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user_name', 'date_posted', 'description', 'picture',
                  'tags', 'likes']
