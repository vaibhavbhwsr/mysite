from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authtoken.models import Token
from registration.models import Post
from django.contrib.auth.models import User


# Created tokens for all existing users.
for user in User.objects.all():
    Token.objects.get_or_create(user=user)


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