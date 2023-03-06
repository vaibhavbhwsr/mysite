from django.urls import path

from chat import consumers


websocket_urlpatterns = [
    path('ws/ajwc/<str:group>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi())
]
