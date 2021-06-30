from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView, TemplateView, \
    View, CreateView, ListView, DetailView
from registration.forms import RegistrationForm, NewPostForm
from registration.models import Post

# Create your views here.


""" APIs """
from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from registration.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions
from rest_framework.authtoken.models import Token


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

""" HTMLs """


# SignUp
class SignupView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/'
    success_message = "%(username)s was created successfully! Now Login with"\
        " the same username and password!"

    # This is necessary function to use with UserPassesTextMixin
    def test_func(self):
        return self.request.user.is_anonymous

    # This function stop accessing signup page to logged in user
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home"))


# Login
class MyLoginView(SuccessMessageMixin, LoginView):
    # Here it stops logged in user to access log in page.
    redirect_authenticated_user = True
    success_message = '%(username)s, Welcome Here!'


# Home Page
# Post Related Views
@ method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Post
    template_name = 'registration/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    extra_context = {'value': 'Create Post'}
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # print(self.request.user)
        # print(Post.objects.all())
        liked = []
        if self.request.user.is_authenticated:
            for post in Post.objects.all():
                # print(post.description)
                for like in post.likes.all():
                    # print(like)
                    if self.request.user == like:
                        liked.append(post)
                        # print('user is:', liked)
                        break
            # Here I passed list of posts, logged user liked by above logic.
            context['liked'] = liked
        return context


# Post Create
@ method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'registration/post/create_post.html'
    success_url = '/'
    success_message = 'Your Post Uploaded Successfully!'
    extra_context = {'value': 'Create'}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.save(commit=False)
        form.instance.user_name = self.request.user
        form.save()
        return super().form_valid(form)


# Post Detail
@ method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'registration/post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        # print(post)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        return context


# Like View
@ method_decorator(login_required, name='dispatch')
class LikeView(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        # id = request.POST.get('sid') # it's a way to get data form ajax
        # print(id, post)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # This calls likes_count() form model = Post
        count = post.likes_count()

        # This change is for ajax logic makes true if liked and vice versa
        is_like = not is_like

        return JsonResponse({'liked': is_like, 'count': count})


# Post Delete
@ method_decorator(login_required, name='dispatch')
class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'registration/post/post_confirm_delete.html'
    success_url = '/deleted/'
    # success_message = 'Your Post Deleted Successfully!'  # Not Working


# Post Update
@ method_decorator(login_required, name='dispatch')
class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'registration/post/create_post.html'
    success_url = '/'
    extra_context = {'value': 'Update'}
    success_message = 'Your Post Updated Successfully!'


# Profile Page
# Profile
@ method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):
    template_name = 'registration/profile/profile.html'


# Profile Update
@ method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView, SuccessMessageMixin):
    model = User
    template_name = 'registration/profile/update_profile.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/'
    success_message = 'Your Profile Updated Successfully!'

    def get_object(self, **kwargs):
        return self.request.user
