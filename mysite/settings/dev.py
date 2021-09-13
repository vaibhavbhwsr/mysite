from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysitedb1',
        'USER': 'postgres',
        'PASSWORD': 'psql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
