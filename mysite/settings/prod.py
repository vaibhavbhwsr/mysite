from .base import *
import django_on_heroku


# Activate Django_on_heroku
django_on_heroku.settings(locals())

ALLOWED_HOSTS = ['mynameheresite.herokuapp.com']
