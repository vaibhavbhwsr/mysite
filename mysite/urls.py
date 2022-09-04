"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


# Main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/post/', permanent=True)),
    path('', include('registration.urls')),
    path('post/', include('post.urls')),
    path('group/', include('group_chat.urls')),
]


# All APIs
api_urls = [
    path(
        'api/v1/',
        include(
            [
                path('auth/', include('rest_framework.urls')),
                path(
                    'registration/',
                    include('registration.api.urls', namespace='registration'),
                ),
                path('post/', include('post.api.urls', namespace='post')),
            ]
        ),
    )
]
urlpatterns += api_urls


# Swagger schema_view
schema_view = get_schema_view(
    openapi.Info(
        title="Mysite API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@mysite.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# When DEBUG is True (Secure practice)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'debug_toolbar' in settings.INSTALLED_APPS:
    urlpatterns.insert(0, path('__debug__/', include('debug_toolbar.urls')))
