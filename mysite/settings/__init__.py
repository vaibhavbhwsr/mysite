'''
Configure this file according:
MODE in settings.ini:
- dev: Development
- prod: Production
- test: Testing (not implemented yet)
'''
from .base import *
from decouple import config

MODE = config("MODE", default='prod')

if MODE == 'dev':
    from .dev import *
elif MODE == 'prod':
    from .prod import *
