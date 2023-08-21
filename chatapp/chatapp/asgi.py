import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chathandler import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = ProtocolTypeRouter(
    application_mapping={
        "http": get_asgi_application(),
        "websocket": URLRouter(
            routing.websocket_urlpatterns
        )
    }
)
