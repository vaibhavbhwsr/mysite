from django.urls import path
from group_chat import views


urlpatterns = [
    path('chat/', views.IndexView.as_view(), name='chat'),
    path('list/', views.GroupListView.as_view(), name='group_list'),
    path('chat/<str:group_name>/', views.GroupChatView.as_view(), name='group_chat'),
]
