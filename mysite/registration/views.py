from .forms import RegistrationForm, NewPostForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class SignupView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/'
    success_message = "%(username)s was created successfully! Login with the same username and password!"


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'registration/profile.html'


class MyLoginView(SuccessMessageMixin, LoginView):
    redirect_authenticated_user = True
    success_message = 'Welcome Here!'


class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'


@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'registration/create_post.html'
    success_url = '/'
    success_message = 'Your Post Created and Uploaded Successfully'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        data = form.save(commit=False)
        form.instance.user_name = self.request.user
        self.object = form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'registration/profile.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'registration/post/detail.html'


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'registration/post/post_confirm_delete.html'
    success_url = '/deleted/'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['description', 'picture', 'tags']
    template_name = 'registration/create_post.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_name:
            return True
        return False
