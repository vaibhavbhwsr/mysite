from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    It converted the user_name.id to user_name.username for API.
    and ReadOnlyField only allows to read username not to Deserialize it.
    we could have also used CharField(read_only=True) here.
    '''
    user_name = serializers.ReadOnlyField(source='user_name.username')

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id', 'user_name', 'date_posted', 'description',
        #           'picture', 'tags', 'likes']
