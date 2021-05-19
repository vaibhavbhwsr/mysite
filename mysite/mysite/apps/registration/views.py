from .forms import RegistrationForm, NewPostForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


# Create your views here.

# SignUp
class SignupView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/'
    success_message = "%(username)s was created successfully! Now Login with the same username and password!"


# Login
class MyLoginView(SuccessMessageMixin, LoginView):
    redirect_authenticated_user = True
    success_message = 'Welcome Here!'


# Logout
class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'


# Home Page
@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Post
    template_name = 'registration/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 10


# Post Related Views
# Post Create
@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'registration/post/create_post.html'
    success_url = '/'
    success_message = 'Your Post Created and Uploaded Successfully'
    extra_context = {'value': 'Create Post'}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        data = form.save(commit=False)
        form.instance.user_name = self.request.user
        self.object = form.save()
        return super().form_valid(form)


# Post Detail
class PostDetailView(DetailView):
    model = Post
    template_name = 'registration/post/detail.html'


# Post Delete
class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'registration/post/post_confirm_delete.html'
    success_url = '/deleted/'
    success_message = 'Your Post Deleted Successfully'


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

