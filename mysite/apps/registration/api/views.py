from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import DjangoModelPermissions

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return User.objects.filter(username=self.request.user)
        else:
            return User.objects.all()


"""
from registration.serializers import PostSerializer
from rest_framework import generics
from registration.serializers import UserSerializer
from rest_framework import permissions
from registration.permissions import IsOwnerReadOnly


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostListCreateApi(generics.ListCreateAPIView):
    # Here IsAuthenticatedOrReadOnly ensure that authenticated requests get
    # read-write access, and unauthenticated requests get read-only access.
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Ye samajh ni aaya ki kaise krra h ye.
    def perform_create(self, serializer):
        print(self.request)
        serializer.save(user_name=self.request.user)


class PostEditApi(generics.RetrieveUpdateDestroyAPIView):
    # Here IsAuthenticatedOrReadOnly described above in PostListApiView
    permission_class = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""
