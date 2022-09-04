from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = '__all__'
