from .forms import RegistrationForm  # Added
from django.views.generic.edit import CreateView


class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/signup.html/'
    # success_url = '/accounts/success/'