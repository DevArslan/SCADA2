from django.urls import path
from . import views

urlpatterns = [
    path('', views.database, name = 'database'),
]



# здесь мы обращаемся к файлу views, который отвечает за выполнение каких-либо действий, например рендер html страницы