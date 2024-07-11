# import json
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_group_name = 'test'

#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()
   

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type':'chat_message',
#                 'message':message
#             }
#         )

#     def chat_message(self, event):
#         message = event['message']

#         self.send(text_data=json.dumps({
#             'type':'chat',
#             'message':message
#         }))


from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    logging.info(f'piyush room_name: {self.room_name}')
    self.room_group_name = f'chat_{self.room_name}'
    

    # Add user to the room group
    await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    await self.accept()

  async def disconnect(self, close_code):
    # Remove user from the room group
    await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

  async def receive(self, text_data):
    data = json.loads(text_data)
    message = data['message']

    # Send message to all users in the room group
    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message,
        }
    )

  async def chat_message(self, event):
    message = event['message']

    # Send message to the websocket
    await self.send(text_data=json.dumps({'message': message}))

