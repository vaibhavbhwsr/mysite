from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView

from django.contrib.auth import get_user_model
from django.db.models import Q
from private_chat.models import OneOneGroup

User = get_user_model()

# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'chat/private_chat/list.html'


@method_decorator(login_required, name='dispatch')
class PrivateChatView(TemplateView):
    template_name = 'chat/private_chat/index.html'

    def get(self, request, *args, **kwargs):
        user1 = request.user
        user2 = User.objects.get(username=kwargs.get('username'))

        try:
            group = OneOneGroup.objects.get(
                (Q(user1=user1) & Q(user2=user2)) | (Q(user1=user2) & Q(user2=user1))
            )
        except OneOneGroup.DoesNotExist:
            group = OneOneGroup.objects.create(user1=user1, user2=user2)

        kwargs['group'] = group
        return super(PrivateChatView, self).get(request, *args, **kwargs)