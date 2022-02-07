from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from group_chat.models import Group
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'chat/index.html'


@method_decorator(login_required, name='dispatch')
class GroupListView(ListView):
    model = Group
    template_name = 'chat/group_chat/list.html'


@method_decorator(login_required, name='dispatch')
class GroupChatView(TemplateView):
    template_name = 'chat/group_chat/index.html'

    def get(self, request, *args, **kwargs):
        group, created = Group.objects.get_or_create(name=kwargs['group_name'])
        kwargs['group'] = group
        return super(GroupChatView, self).get(request, *args, **kwargs)
