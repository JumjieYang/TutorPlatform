import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from chat.models import Message


def message_to_json(message):
    return {
        'id': str(message.id),
        'author': message.author.username,
        'content': message.content,
        'created_at': str(message.created_at)
    }


def messages_to_json(messages):
    result = []
    for message in messages:
        result.append(message_to_json(message))
    return result


class ChatConsumer(WebsocketConsumer):

    def init_chat(self, data):
        username = data['username']
        user, created = User.objects.get_or_create(username=username)
        content = {
            'command': 'init_chat'
        }
        if not user:
            content['error'] = 'Unable to get or create User with username: ' + username
            self.send_message(content)
        content['success'] = 'Chatting in with success with username: ' + username
        self.send_message(content)

    def fetch_messages(self, data):
        messages = Message.past_messages(roomNumber=data['roomNumber'])
        content = {
            'command': 'messages',
            'messages': messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from']
        text = data['text']
        author_user, created = User.objects.get_or_create(username=author)
        message = Message.objects.create(author=author_user, content=text)
        content = {
            'command': 'new_message',
            'message': message_to_json(message)
        }
        self.send_chat_message(content)

    commands = {
        'init_chat': init_chat,
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = 'room'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # leave group room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))