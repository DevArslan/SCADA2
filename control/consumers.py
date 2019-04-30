import asyncio
import psycopg2
from channels.consumer import AsyncConsumer
from django.db.models.signals import post_save


class ChartConsumer(AsyncConsumer):

	async def websocket_connect(self, event):
		print ('connection successfull', event)

		await self.send({
			'type': 'websocket.accept'
			})

	



