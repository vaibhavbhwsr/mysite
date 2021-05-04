from .forms import RegistrationForm  		# Added
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/signup.html/'
    success_url = '/success/'


class DashboardView(TemplateView):
	template_name = 'users/dashboard.html'


class MyLoginView(LoginView):
	template_name = 'users/login.html'


class MyPassChangeView(PasswordChangeView):
	template_name = 'users/passwordchange.html'
	success_url = '/passchangedone/'


class MyPassChangeDoneView(PasswordChangeDoneView):
	template_name = 'users/passchangedone.html'


class MyLogoutView(LogoutView):				# It needs update in success_url of passwordchange, here changes made
	template_name = 'users/logout.html'		# in view MyPassChangeView.
	