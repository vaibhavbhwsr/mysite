from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name='video_chat'),
    path('room/', views.room),
    path('get-token/', views.get_token),
    path('create-member/', views.create_member),
    path('get-member/', views.get_member),
    path('delete-member/', views.delete_member),
    path('start-recording/', views.start_recording),
    path('stop-recording/', views.stop_recording),
    path('recordings/', views.MeetRecordListView.as_view(), name='meet_recordings'),
    path('record-detail/<int:pk>', views.MeetRecordDetailView.as_view(), name='record_detail'),
]
