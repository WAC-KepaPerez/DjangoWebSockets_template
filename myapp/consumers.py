import asyncio
import datetime
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

class ContarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.send(text_data=json.dumps({'message': 'disconnected'}))

    async def receive(self, text_data, bytes_data=None):
        data = json.loads(text_data)
        numero = data.get('numero')
        for i in range(1, int(numero) + 1):
            await asyncio.sleep(3)
            timestamp = datetime.datetime.now().time()
            await self.send(text_data=json.dumps({'message': 'Contando {}'.format(i),'timestamp': str(timestamp),'count':i}))
        await self.close()  # Disconnect after sending messages


            