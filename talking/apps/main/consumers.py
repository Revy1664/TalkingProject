import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept() # accept all connections

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message})) # senf answer message to client

    def disconnect(self, close_code):
        pass