import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        for i in range(5):
            await asyncio.sleep(3)
            await self.send(text_data=json.dumps({'message': 'Hello! This is message number {}'.format(i+1)}))