from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView

from group_chat.forms import NewGroupForm
from group_chat.models import Group

# Create your views here.


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'chat/index.html'


@method_decorator(login_required, name='dispatch')
class GroupListView(ListView):
    model = Group
    template_name = 'chat/group_chat/list.html'


class CreateGroupView(CreateView):
    form_class = NewGroupForm
    template_name = 'chat/group_chat/create_group.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            data = {'id': self.object.id, 'name': self.object.name}
            return JsonResponse(
                {
                    "data": data,
                    "success": True,
                    "message": "Group Created Successfully!",
                },
                status=HTTPStatus.CREATED,
            )
        else:
            return JsonResponse(
                {
                    "data": form.errors,
                    "success": False,
                    "message": "Something Went Wrong!",
                },
                status=HTTPStatus.NOT_ACCEPTABLE,
            )


@method_decorator(login_required, name='dispatch')
class GroupChatView(TemplateView):
    template_name = 'chat/group_chat/index.html'

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(name=kwargs['group_name'])
        kwargs['group'] = group
        return super(GroupChatView, self).get(request, *args, **kwargs)
