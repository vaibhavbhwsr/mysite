from .base import *
import django_on_heroku
import dj_database_url

# Activate Django_on_heroku
django_on_heroku.settings(locals())

ALLOWED_HOSTS = ['mynameheresite.herokuapp.com']

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
