# from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DATABASE_NAME', default='mysitedb'),
#         'USER': config('DATABASE_USER', default='postgres'),
#         'PASSWORD': config('DATABASE_PASSWORD', default='psql'),
#         'HOST': config('DATABASE_HOST', default='localhost'),
#         'PORT': config('DATABASE_PORT', default=5432),
#     }
# }

from .base import *
import django_on_heroku
import dj_database_url

# Activate Django_on_heroku
django_on_heroku.settings(locals())

ALLOWED_HOSTS = ['mynameheresite.herokuapp.com']

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
