import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


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
    """Can only be done is ACL is enabled and bucket has public access"""
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


def get_presigned_url(s3_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AGORA_STORAGE_ACCESSKEY,
        aws_secret_access_key=settings.AGORA_STORAGE_SECRETKEY,
        region_name=settings.AGORA_AWS_S3_REGION_NAME,
        config=Config(signature_version='s3v4')
    )

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': settings.AGORA_STORAGE_BUCKET,
            'Key': s3_key
        },
        ExpiresIn=3600
    )

    return url
