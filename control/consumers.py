import asyncio
import select
import psycopg2
from channels.db import database_sync_to_async
import psycopg2.extensions
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models.signals import post_save



class ChartConsumer(AsyncConsumer):
	


	async def websocket_connect(self, event):
		print ('connection successfull', event)
		
		await self.send({
			'type': 'websocket.accept'
			})
		
		
	async def websocket_receive(self, event):
		
		if event.get("text") == "OFF":
			print("OFF")

		if event.get("text") == "ON":

			var = await self.get_data_opc(event)	
			await self.send({
			'type': 'websocket.send',
			'text': var,

			})


	@database_sync_to_async
	def get_data_opc(self,event):

		conn = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
		conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

		curs = conn.cursor()
		curs.execute("LISTEN events;")

		print ("Waiting for notifications on channel 'DatasetOPC'")
		while event.get("text") == "ON":
		    if select.select([conn],[],[],2) == ([],[],[]):
		        print ("Timeout")
		    else:
		        conn.poll()
		        while conn.notifies:
		            notify = conn.notifies.pop(0)
		            return (notify.payload)	
	