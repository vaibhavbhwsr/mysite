from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('api/', include('registration.api.urls')),
    # """ HTMLs URLConfigs """
    # Without Logged in
    # path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/login/', views.MyLoginView.as_view(), name='login'),
    # Password Reset
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/pass/password_reset_email.html'
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/pass/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/pass/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/pass/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
    # Logout
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # MyProfile Page
    path('profile/', views.MyProfileView.as_view(), name='profile'),
    path('update/', views.UpdateProfileView.as_view(), name='update-profile'),
    # Password change
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name="registration/pass_2/password_change_form.html"
        ),
        name='password_change',
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/pass_2/password_change_done.html"
        ),
        name='password_change_done',
    ),
]
