from email.mime import application
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from home.consumers import mentalHealth_care
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mentalHealth_care.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        URLRouter([
            path('ws/',mentalHealth_care.as_asgi())
        ])
    )
})