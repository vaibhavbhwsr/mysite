from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import RegistrationForm, NewPostForm
from django.views.generic import View, CreateView, ListView, DetailView
from django.views.generic import DeleteView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.

# SignUp
class SignupView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/'
    success_message = "%(username)s was created successfully! Now Login with"
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


# Logout
class MyLogoutView(SuccessMessageMixin, LogoutView):
    template_name = 'registration/logout.html'
    success_message = 'Successfully Logged Out!'


# Home Page
# Post Related Views
@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Post
    template_name = 'registration/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 10


# Post Create
@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'registration/post/create_post.html'
    success_url = '/'
    success_message = 'Your Post Uploaded Successfully'
    extra_context = {'value': 'Create Post'}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.save(commit=False)
        form.instance.user_name = self.request.user
        self.object = form.save()
        return super().form_valid(form)


# Post Detail
@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'registration/post/detail.html'


# Like View
class LikeView(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Post.object.get(pk=pk)
        # id = request.POST.get('sid')

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        return JsonResponse({'liked': is_like})


# class LikeView(LoginRequiredMixin, View):

#     def post(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(pk=pk)

#         is_like = False

#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 break

#         if not is_like:
#             post.likes.add(request.user)

#         if is_like:
#             post.likes.remove(request.user)

#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)


# Post Delete
class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'registration/post/post_confirm_delete.html'
    success_url = '/deleted/'
    success_message = 'Your Post Deleted Successfully'  # Not Working


# Post Update
class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'registration/post/create_post.html'
    success_url = '/'
    extra_context = {'value': 'Update Post'}
    success_message = 'Your Post Updated Successfully!'


# Profile Page
# Profile
class MyProfileView(TemplateView):
    template_name = 'registration/profile/profile.html'


# Profile Update
class UpdateProfileView(UpdateView):
    model = User
    template_name = 'registration/profile/update_profile.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/'
    success_message = 'Your Profile Updated Successfully!'

    def get_object(self):
        return self.request.user
