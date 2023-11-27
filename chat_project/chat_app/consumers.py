# chat_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

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


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f'chat_{self.chat_id}',
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('text', '')  # Используйте get для избежания ошибки KeyError
        print(f"Received message in consumer: {message}")
        await self.channel_layer.group_send(
            f'chat_{self.chat_id}',
            {
                'type': 'chat_message',
                'sender': 'Me',
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
