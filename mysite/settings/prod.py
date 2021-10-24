from .base import *
import django_on_heroku


# Activate Django_on_heroku
django_on_heroku.settings(locals())

ALLOWED_HOSTS = ['mynameheresite.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME', default='postgresql-cylindrical-45367'),
        'USER': config('DATABASE_USER', default='wppagmcsjwqzzn'),
        'PASSWORD': config('DATABASE_PASSWORD', default='f394cae348b2a1e4dea982e08dbc7fd08c75dd916d74d62c34902fb4c388b4b1'),
        'HOST': config('DATABASE_HOST', default='ec2-34-194-120-237.compute-1.amazonaws.com'),
        'PORT': config('DATABASE_PORT', default=5432),
    }
}
