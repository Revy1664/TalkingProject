import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

asgi_app = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talking.settings')

application = ProtocolTypeRouter(
    {
        "http": asgi_app,
    }
)