import boto3
from botocore.exceptions import ClientError
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'private-media'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False



def make_file_public(file_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    try:
        s3.put_object_acl(
            Bucket=settings.AGORA_STORAGE_BUCKET,
            Key=file_name,
            ACL='public-read'
        )
        return True
    except ClientError as e:
        # Handle any errors that occurred during setting ACL
        print(f"Error setting object ACL: {e}")
        return False
