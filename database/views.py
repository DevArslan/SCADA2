from django.shortcuts import render
from django.http import HttpResponse

def database(request):
	return (render(request, 'database.html'))

# функция render возвращается html страницу

