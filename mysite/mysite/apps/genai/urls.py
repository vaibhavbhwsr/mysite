from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='genai'),
    path('content', views.GenerateContentView.as_view(), name='content'),
]
