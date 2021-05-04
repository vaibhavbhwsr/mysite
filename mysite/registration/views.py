from .forms import RegistrationForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html/'
    success_url = '/accounts/success/'

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
	template_name = 'registration/profile.html'