import base64
import json
import requests
import random
from agora_token_builder import RtcTokenBuilder
import time
from django.conf import settings

MODE = 'web'
APP_ID = settings.AGORA_APP_ID
CUSTOMER_KEY = settings.AGORA_CUSTOMER_KEY
CUSTOMER_SECRET = settings.AGORA_CUSTOMER_SECRET
APP_CERTIFICATE = settings.AGORA_APP_CERTIFICATE
AGORA_STORAGE_VENDOR = settings.AGORA_STORAGE_VENDOR
AGORA_STORAGE_REGION = settings.AGORA_STORAGE_REGION
AGORA_STORAGE_BUCKET = settings.AGORA_STORAGE_BUCKET
AGORA_STORAGE_ACCESSKEY = settings.AGORA_STORAGE_ACCESSKEY
AGORA_STORAGE_SECRETKEY = settings.AGORA_STORAGE_SECRETKEY


def generate_token(channel, uid):
    expirtionTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirtionTimeInSeconds
    role = 1  # 1 for host and 2 for guest(doesn't cared here for now)

    token = RtcTokenBuilder.buildTokenWithUid(APP_ID, APP_CERTIFICATE, channel, uid, role, privilegeExpiredTs)
    return token


def get_headers():
    credentials = CUSTOMER_KEY + ':' + CUSTOMER_SECRET
    # Encode with base64
    base64_credentials = base64.b64encode(credentials.encode('utf8'))
    credential = base64_credentials.decode('utf8')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}'
    }
    return headers


def get_uid_and_token_for_recording(channel):
    uid = random.randint(100001, 4294967295)
    token = generate_token(channel, uid)
    return (uid, token)


def call_acquire(channel, uid):
    url = f'https://api.agora.io/v1/apps/{APP_ID}/cloud_recording/acquire'
    headers = get_headers()
    payload = {
        'cname': channel,
        'uid': str(uid),
        'clientRequest': {'resourceExpiredHour': 24, 'scene': 1}
    }
    response = requests.post(url=url, json=payload, headers=headers)
    return response


def call_start(resource_id, channel, uid, token):
    url = f'https://api.agora.io/v1/apps/{APP_ID}/cloud_recording/resourceid/{resource_id}/mode/{MODE}/start'
    headers = get_headers()
    payload = {
        'uid': str(uid),
        'cname': channel,
        'clientRequest': {
            'token': token,
            'recordingConfig': {
                'channelType': 0,
                'maxIdleTime': 30,
                'audioProfile': 1,
                'videoStreamType': 0,
            },
            'extensionServiceConfig': {
                'errorHandlePolicy': 'error_abort',
                'extensionServices': [
                    {
                        'serviceName': 'web_recorder_service',
                        'errorHandlePolicy': 'error_abort',
                        'serviceParam': {
                            'url': f'{settings.BASE_URL}/video-chat/room/?channel={channel}&uid={uid}&token={token}&name=rec-fireshine',
                            'audioProfile': 0,
                            'videoWidth': 1920,
                            'videoHeight': 1080,
                            'maxRecordingHour': 72
                        }
                    }
                ]
            },
            'recordingFileConfig': {'avFileType': ['hls', 'mp4']},
            'storageConfig': {
                'vendor': int(AGORA_STORAGE_VENDOR),
                'region': int(AGORA_STORAGE_REGION),
                'bucket': AGORA_STORAGE_BUCKET,
                'accessKey': AGORA_STORAGE_ACCESSKEY,
                'secretKey': AGORA_STORAGE_SECRETKEY,
                'fileNamePrefix': [f'{channel}', f'{uid}'],
            },
        },
    }
    response = requests.post(url=url, json=payload, headers=headers)
    return response


def call_stop(resource_id, sid, channel, record_uid):
    url = f'https://api.agora.io/v1/apps/{APP_ID}/cloud_recording/resourceid/{resource_id}/sid/{sid}/mode/{MODE}/stop'
    headers = get_headers()
    payload = {
        'cname': channel,
        'uid': record_uid,
        'clientRequest': {}
    }
    response = requests.post(url=url, json=payload, headers=headers)
    return response
