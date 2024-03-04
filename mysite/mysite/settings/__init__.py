'''
Configure this file according:
MODE in settings.ini:
- dev: Development
- prod: Production
- test: Testing (not implemented yet)
'''
from .base import *                                 # noqa: F403
from decouple import config

MODE = config("MODE", default='prod')

if MODE == 'dev':
    from .dev import *                              # noqa: F403
elif MODE == 'prod':
    from .prod import *                             # noqa: F403


# Some lines to check setting being used
print()
print('############################### Settings Check ################################')
print(f'Hosts: {ALLOWED_HOSTS}')                    # noqa: F405
print(f'Mode: {MODE}')
print(f'Debug: {DEBUG}')                            # noqa: F405
print(f'Use S3: {USE_S3}')                          # noqa: F405
print(f'Static URL: {STATIC_URL}')                  # noqa: F405
print(f'Media URL: {MEDIA_URL}')                    # noqa: F405
print(f'Database: {DATABASES["default"]["HOST"]}')  # noqa: F405
print('###############################################################################')
