from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # Home page
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/like', views.LikeView.as_view(), name='like'),

    # Create Post page
    path('create/post/', views.PostCreateView.as_view(), name='create-post'),

    # Detail page
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('deleted/', login_required(TemplateView.as_view(template_name='post/post_delete.html')), name='deleted'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),

    # Post Comment
    path('create/comment/<int:pk>', views.PostCommentView.as_view(), name='create-comment'),
]
