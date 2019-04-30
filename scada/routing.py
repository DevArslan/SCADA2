#from django.conf.urls import  url
from django.urls import path, include
from control.consumers import ChartConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack





application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
			URLRouter([
    			path("control/", ChartConsumer) 
			]),
		),
	})

