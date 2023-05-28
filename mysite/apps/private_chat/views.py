from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView

from django.contrib.auth import get_user_model

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
        user = User.objects.get(username=kwargs['username'])
        kwargs['user'] = user
        return super(PrivateChatView, self).get(request, *args, **kwargs)