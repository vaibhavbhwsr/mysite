from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "post"

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')


urlpatterns = [
    # """ APIs URLConfigs """
    path('', include(router.urls))
]
