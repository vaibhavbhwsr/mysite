from django import forms
from .models import Post  # , Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'picture', 'tags']


# # Not Used
# class PostCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment_text']
