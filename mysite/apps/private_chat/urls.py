from django.urls import path

from private_chat import views


urlpatterns = [
    path('list/', views.UserListView.as_view(), name='user_list'),
]