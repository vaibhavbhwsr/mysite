from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Without auth user
    # path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/login/', views.MyLoginView.as_view(), name='login'),

    # With auth user
    # Feed Post( Home, Detail, Post-Update, Delete, logout ...)
    path('', views.HomeView.as_view(), name='home'),
    path('create/post/', views.PostCreateView.as_view(), name='create-post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('deleted/', TemplateView.as_view(template_name='registration/post/post_delete.html'), name='deleted'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('accounts/logout/', views.MyLogoutView.as_view(), name='logout'),

    # Profile
    path('profile/', views.MyProfileView.as_view(), name='profile'),
    path('update/', views.UpdateProfileView.as_view(), name='update-profile'),
]
