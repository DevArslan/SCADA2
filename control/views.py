from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, time, random



def chart(request):
	con = None
	con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
	cur = con.cursor()
	cur.execute("SELECT * FROM DataOPC")
	data = cur.fetchall()
	
	number = [x[0] for x in data]
	value = [x[1] for x in data]
	cur.close()
	con.close()


	return render(request, 'chart.html',{'dataset_value': value, 'dataset_number': number})










