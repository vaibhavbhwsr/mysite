from .base import ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE

ALLOWED_HOSTS += ['*', ]    # Later remove star

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]
