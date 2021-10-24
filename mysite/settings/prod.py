from .base import *
import django_on_heroku
import dj_database_url

# Activate Django_on_heroku
django_on_heroku.settings(locals())

ALLOWED_HOSTS = ['mynameheresite.herokuapp.com']

# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {'default': dj_database_url.config(default='postgres://wppagmcsjwqzzn:f394cae348b2a1e4dea982e08dbc7fd08c75dd916d74d62c34902fb4c388b4b1@ec2-34-194-120-237.compute-1.amazonaws.com:5432/dfa0ssdi19ssr6')}
