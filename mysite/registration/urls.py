from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('success/', TemplateView.as_view(template_name='registration/success.html'), name='success'),
	path('', include('django.contrib.auth.urls')),
	path('profile/', views.ProfileView.as_view(), name='profile'),
]
