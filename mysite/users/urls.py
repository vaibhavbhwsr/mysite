from django.urls import path
from . import views
from django.contrib.auth.urls import views  as auth_view
from django.views.generic.base import TemplateView

urlpatterns = [
	path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
	path('signup/', views.SignupView.as_view(), name="signup"),
	path('dashboard/', TemplateView.as_view(template_name='users/dashboard.html'), name='dashboard'),
	path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]		