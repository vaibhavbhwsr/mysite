from django.urls import path

from private_chat import consumers


websocket_urlpatterns = [
    path('ws/ajwc/private/<str:group>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]
