from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, random
import json


def database(request):

	con = None
	con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
	cur = con.cursor()
	cur.execute("SELECT * FROM DATA_TABLE")
	data = cur.fetchall()

	number = [x[0] for x in data]
	date = [x[1] for x in data]
	name = [x[2] for x in data]
	size = [x[3] for x in data]

	cur.close()
	con.close()


	return (render(request, 'database.html',{'number_array': number,'date_array': date,'name_array': name,'size_array': size}))

















