from django.urls import path
from . consumers import ChatHandler
websocket_urlpatterns = [
    path('chat',ChatHandler.as_asgi())
]