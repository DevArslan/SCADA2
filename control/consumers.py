import asyncio
import select
import psycopg2
from channels.db import database_sync_to_async
import psycopg2.extensions
from channels.consumer import AsyncConsumer
from django.db.models.signals import post_save



class ChartConsumer(AsyncConsumer):
	


	async def websocket_connect(self, event):
		print ('connection successfull', event)
		
		await self.send({
			'type': 'websocket.accept'
			})
		for i in range (1,10):
			var = await self.get_data_opc()	
			await self.send({
			'type': 'websocket.send',
			'text': var,
			})
			await asyncio.sleep(2)
		
		

	@database_sync_to_async
	def get_data_opc(self):

		conn = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
		conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

		curs = conn.cursor()
		curs.execute("LISTEN events;")

		print ("Waiting for notifications on channel 'DataOPC'")
		while True:
		    if select.select([conn],[],[],2) == ([],[],[]):
		        print ("Timeout")
		    else:
		        conn.poll()
		        while conn.notifies:
		            notify = conn.notifies.pop(0)
		            return (notify.payload)	

#notify.pid , notify.channel,
	