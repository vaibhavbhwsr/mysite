from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import (
    UpdateView,
    TemplateView,
    CreateView,
)
from .forms import RegistrationForm

# Create your views here.


# SignUp
class SignupView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/'
    success_message = (
        "%(username)s was created successfully! Now Login with"
        " the same username and password!"
    )

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


# Profile Page
# Profile
@method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):
    template_name = 'registration/profile.html'


# Profile Update
@method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView, SuccessMessageMixin):
    model = User
    template_name = 'registration/update_profile.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/'
    success_message = 'Your Profile Updated Successfully!'

    def get_object(self, **kwargs):
        return self.request.user
