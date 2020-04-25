import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def init_chat(self, data):
        username = data['username']
        user = User.objects.get(username=username)
        content = {
            'command': 'init_chat'
        }
        if not user:
            content['error'] = 'Unable to get User with username : ' + username
        content['success'] = 'Chatting success with username : ' + username
        await self.send(text_data=json.dumps(content))

    async def fetch_messages(self, data):
        messages = Message.objects.filter(room=self.room_name).order_by('-created_at').all()[:50]
        messages_list = []
        for message in messages:
            messages_list.append({
                'id': str(message.id),
                'author': message.author.username,
                'content': message.content,
                'created_at': str(message.created_at)
            })
        content = {
            'command': 'messages',
            'messages': messages_list
        }
        await self.send(text_data=json.dumps(content))

    async def new_message(self, data):
        author, text = data['from'], data['text']
        author = User.objects.get(username=author)
        message = Message.objects.create(author=author, content=text, room=self.room_name)
        message.save()
        content = {
            'command': 'new_message',
            'message': {
                'id': str(message.id),
                'author': message.author.username,
                'content': message.content,
                'created_at': str(message.created_at)
            }
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': content
            }
        )

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))