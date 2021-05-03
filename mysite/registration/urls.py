from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('success/', TemplateView.as_view(template_name='registration/success.html'), name='success'),
	path('', include('django.contrib.auth.urls')),
	path('profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
]
