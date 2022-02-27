from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from group_chat.models import Group


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        user = self.scope['user']
        content['user'] = user.username
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        if user.is_authenticated:
            chat = await database_sync_to_async(group.group_chat.create)(
                content=content['msg'], user=user
            )
            await self.channel_layer.group_send(
                self.group_name, {'type': 'chat.message', 'message': content}
            )
        else:
            await self.send_json({'msg': 'Login Required', 'user': 'guest'})

    async def chat_message(self, event):
        await self.send_json(event['message'])

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
