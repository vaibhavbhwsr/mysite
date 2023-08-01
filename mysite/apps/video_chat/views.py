import json
import random

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import utils
from .models import RoomMember, MeetRecord

# Create your views here.

APP_ID = settings.AGORA_APP_ID


def get_token(request):
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    token = utils.generate_token(channelName, uid)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)


def lobby(request):
    return render(request, 'chat/video_chat/lobby.html')


def room(request):
    for data in request.GET:
        request.session[data] = request.GET[data]
    return render(request, 'chat/video_chat/room.html')


@csrf_exempt
def create_member(request):
    data = json.loads(request.body)

    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name'],
    )
    data = {'name': data['name']}

    return JsonResponse(data, safe=False)


def get_member(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name
    )

    name = member.name
    return JsonResponse({'name': name}, safe=False)


@csrf_exempt
def delete_member(request):
    data = json.loads(request.body)

    member = RoomMember.objects.filter(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    if member.exists():
        member.first().delete()

    return JsonResponse('Member was deleted', safe=False)


def start_recording(request):
    channel = request.GET['channel']
    uid, token = utils.get_uid_and_token_for_recording(channel)
    acquire_response = utils.call_acquire(channel, uid)

    if acquire_response.status_code == 200:
        resource_id = acquire_response.json()['resourceId']
        start_response = utils.call_start(resource_id, channel, uid, token)
        if start_response.status_code == 200:
            return_response = {'record_uid': uid, 'sid': start_response.json()['sid'], 'resource_id': resource_id}
        else:
            return_response = start_response.json()
    else:
        return_response = acquire_response.json()

    return JsonResponse(return_response, safe=False)


def stop_recording(request):
    channel = request.GET['channel']
    record_uid = request.GET['record_uid']
    sid = request.GET['sid']
    resource_id = request.GET['resource_id']

    response = utils.call_stop(resource_id, sid, channel, record_uid)
    response = response.json()
    for i in response.get('serverResponse').get('extensionServiceState'):
        for key, value in i.items():
            if 'fileList' in value:
                for j in value['fileList']:
                    for k, v in j.items():
                        if k == 'filename':
                            if v.split('.')[-1] == 'mp4':
                                link = v
    link = f'https://{settings.AGORA_STORAGE_BUCKET}.s3.amazonaws.com/{channel}/{str(record_uid)}/{link}'
    obj = MeetRecord.objects.create(channel=channel, record_link=link)
    return JsonResponse(response, safe=False)
