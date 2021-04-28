from django.urls import path
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('success/', views.SuccessView.as_view(), name='success'),
]