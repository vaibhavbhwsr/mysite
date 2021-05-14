from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('accounts/login/', views.MyLoginView.as_view(), name='login'),
	path('accounts/logout/', views.MyLogoutView.as_view(), name='logout'),
	# path('', include('django.contrib.auth.urls')),
	path('profile', views.ProfileView.as_view(), name='profile'),

	# Post urls
	path('createpost/', views.PostCreateView.as_view(), name='createpost'),
	path('', views.PostListView.as_view(), name='post'),
	path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
	path('delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
	path('deleted/', TemplateView.as_view(template_name='registration/post/post_delete.html'), name='deleted'),
	path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
]
