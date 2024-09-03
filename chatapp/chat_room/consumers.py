import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chat_room.models import Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "test"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        

    def receive(self, text_data):
        curr_user = self.scope["user"]
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        new_message = Message.objects.create(user=curr_user, content=message)
        new_message_id = new_message.user_id

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": curr_user,
                "message_foreign_id": new_message_id
            }
        )

    def chat_message(self, event):
        message = event["message"]
        curr_user_username = event["username"].username
        curr_user_id = event["username"].pk
        message_id = event["message_foreign_id"]

        self.send(text_data=json.dumps({
            "type": "chat",
            "message": message,
            "username": curr_user_username,
            "user_id": curr_user_id,
            "message_foreign_id": message_id
        }))