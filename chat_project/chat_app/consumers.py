import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs'].get('room_name', None)
        if self.chat_id is not None:
            await self.channel_layer.group_add(
                f'chat_{self.chat_id}',
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def exit_chat(self, event):
        await self.channel_layer.group_discard(
            f'chat_{self.chat_id}',
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f'chat_{self.chat_id}',
            self.channel_name
        )

    @database_sync_to_async
    def get_sender_user(self):
        return self.scope["user"]

    async def receive(self, text_data):
        data = json.loads(text_data)
        if 'exit' in data and data['exit']:
            await self.exit_chat(data)
        else:
            message = data.get('text', '')
            sender = await self.get_sender_user()
            print(f"Received message in consumer: {message} from {sender.username}")
            await self.channel_layer.group_send(
                f'chat_{self.chat_id}',
                {
                    'type': 'chat_message',
                    'sender': sender.username,
                    'message': message,
                }
            )

    async def chat_message(self, event):
        sender = event['sender']
        message = event['message']
        print(f"Sending message to client: {message}")
        await self.send(text_data=json.dumps({
            'sender': sender,
            'message': message,
        }))