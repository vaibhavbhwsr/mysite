from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # APIs URLConfigs

    # Add login/logout to API
    path('api-auth/', include('rest_framework.urls')),
    path('usersapi/', views.UserListApiView.as_view()),
    path('usersapi/<int:pk>', views.UserDetailApiView.as_view()),
    path('postsapi/', views.PostListApiView.as_view()),
    path('postsapi/<int:pk>', views.PostDetailApiView.as_view()),


    # HTMLs URLConfigs

    # Without Logged in
    # path('', include('django.contrib.auth.urls')),
    path(
        'signup/',
        views.SignupView.as_view(),
        name='signup'
    ),
    path(
        'accounts/login/',
        views.MyLoginView.as_view(),
        name='login'
    ),
    # Password Reset
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/pass/password_reset_email.html'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/pass/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/pass/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/pass/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    # With Logged in
    # Feed Post( Home, Detail, Post-Update, Delete, logout ...)
    # Home page
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'post/<int:pk>/like',
        views.LikeView.as_view(),
        name='like'
    ),
    # Create Post page
    path(
        'create/post/',
        views.PostCreateView.as_view(),
        name='create-post'
    ),

    # Detail page
    path(
        'detail/<int:pk>/',
        views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        'delete/<int:pk>/',
        views.PostDeleteView.as_view(),
        name='post-delete'
    ),
    path(
        'deleted/',
        login_required(TemplateView.as_view(
            template_name='registration/post/post_delete.html')),
        name='deleted'
    ),
    path(
        'post/<int:pk>/update/',
        views.PostUpdateView.as_view(),
        name='post-update'
    ),

    # Logout
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # MyProfile Page
    path(
        'profile/',
        views.MyProfileView.as_view(),
        name='profile'
    ),
    path(
        'update/',
        views.UpdateProfileView.as_view(),
        name='update-profile'
    ),
    # Password change
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name="registration/profile/password_change_form.html"),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/profile/password_change_done.html"),
        name='password_change_done'
    ),
]
