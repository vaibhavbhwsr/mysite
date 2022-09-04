from decouple import config

from .base import ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE

ALLOWED_HOSTS += ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE.insert(0,  "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]
