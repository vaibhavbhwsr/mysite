from .forms import RegistrationForm
from django.views.generic import CreateView


# Create your views here.

class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/accounts/success/'
