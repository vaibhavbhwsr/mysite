from decouple import config

from .base import ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE, CSRF_TRUSTED_ORIGINS

ALLOWED_HOSTS += ['*', ]    # Later remove star

CSRF_TRUSTED_ORIGINS += ['http://localhost']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE.insert(0,  'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]
