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


# Some lines to check setting being used
print()
print('############################### Settings Check ################################')
print(f'Mode: {MODE}')
print(f'Debug: {DEBUG}')
print(f'Use S3: {USE_S3}')
print(f'Static URL: {STATIC_URL}')
print(f'Media URL: {MEDIA_URL}')
print(f'Database: {DATABASES["default"]["HOST"]}')
print('###############################################################################')
