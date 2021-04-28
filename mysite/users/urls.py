from django.urls import path															# Added line
from . import views

urlpatterns = [
	path('', views.sign_up, name="signup")												# Added
]		