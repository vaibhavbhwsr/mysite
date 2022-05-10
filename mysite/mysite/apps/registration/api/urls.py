from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "registration"

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')


urlpatterns = [
    # """ APIs URLConfigs """
    path('', include(router.urls)),
    # # Add login/logout to API
    # path('users/api/', views.UserListApiView.as_view()),
    # path('users/api/<int:pk>', views.UserDetailApiView.as_view()),
    # path('posts/api/', views.PostListCreateApi.as_view()),
    # path('posts/api/<int:pk>', views.PostEditApi.as_view()),
]
