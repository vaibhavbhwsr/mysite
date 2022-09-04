from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    user_name = models.ForeignKey(
        'auth.User', related_name="posts", on_delete=models.CASCADE
    )  # API also
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='images/post', blank=True)
    tags = models.CharField(max_length=100, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comment = models.ManyToManyField(User, through='Comment')  # Not necessary

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('detail', args=[str(self.pk)])

    def send_index(self):
        return self.pk

    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='post_comment', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'auth.User', related_name='user_comment', on_delete=models.CASCADE
    )
    comment_text = models.TextField()
