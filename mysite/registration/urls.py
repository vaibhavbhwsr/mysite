from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('success/', TemplateView.as_view(template_name='registration/success.html'), name='success'),
	path('accounts/login/', views.MyLoginView.as_view(), name='login'),
	path('accounts/logout/', views.MyLogoutView.as_view(), name='logout'),
	# path('', include('django.contrib.auth.urls')),
	path('', views.ProfileView.as_view(), name='profile'),

	# Post urls
	path('createpost/', views.PostCreateView.as_view(), name='createpost'),
]
