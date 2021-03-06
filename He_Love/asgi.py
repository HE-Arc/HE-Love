import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'He_Love.settings')

import django
django.setup()
import He_Loveapp.routing



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
      "websocket": AuthMiddlewareStack(
        URLRouter(
            He_Loveapp.routing.websocket_urlpatterns
        )
    ),
})