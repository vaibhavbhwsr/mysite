from django.urls import path
from . import views
from django.contrib.auth.urls import views  as auth_view
from django.views.generic.base import TemplateView


urlpatterns = [
	path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
	path('signup/', views.SignupView.as_view(), name="signup"),
	path('success/', TemplateView.as_view(template_name='users/success.html'), name="success"),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('login/', views.MyLoginView.as_view(), name='login'),
	path('passwordchange/', views.MyPassChangeView.as_view(), name='passwordchange'),
	path('passchangedone/', views.MyPassChangeDoneView.as_view(), name='passchangedone'),
	path('logout/', views.MyLogoutView.as_view(), name='logout'),
]		