from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('users', views.UserViewSet, basename='users')


urlpatterns = [

    # """ APIs URLConfigs """

    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),


    # # Add login/logout to API
    # path('users/api/', views.UserListApiView.as_view()),
    # path('users/api/<int:pk>', views.UserDetailApiView.as_view()),
    # path('posts/api/', views.PostListCreateApi.as_view()),
    # path('posts/api/<int:pk>', views.PostEditApi.as_view()),
]
