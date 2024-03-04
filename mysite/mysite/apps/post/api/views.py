from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from post.models import Post

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_name=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        elif not self.request.user.is_anonymous:
            return Post.objects.filter(user_name=self.request.user)
        else:
            return Post.objects.all()
