from .forms import RegistrationForm, NewPostForm
from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


# Create your views here.

class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/success/'


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'registration/profile.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True


class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'


@method_decorator(login_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'registration/create_post.html'
    success_url = '/'

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
