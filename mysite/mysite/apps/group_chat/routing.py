from django.urls import path

from group_chat import consumers


websocket_urlpatterns = [
    path('ws/ajwc/public/<str:group>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi())
]
