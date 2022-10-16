import os
from .base import BASE_DIR, ALLOWED_HOSTS
from decouple import config


ALLOWED_HOSTS += ['*']

# USE_S3 in case for using S3 or not
USE_S3 = config('USE_S3', default=False, cast=bool)

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', None)
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', None)
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', None)
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'commons.storage_backends.StaticStorage'

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'commons.storage_backends.PublicMediaStorage'

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Disabling DjangoRestFramework Browsable API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Database for prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}
