from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View

from . import utils

# Create your views here.


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "genai/index.html"


class GenAIView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "genai/content/index.html")

    def post(self, request, *args, **kwargs):
        input = request.POST.get('user_input')
        generated_text = utils.ai_content_generate(input)
        return JsonResponse(
            {
                "generated_text": generated_text,
                "success": True,
            },
            status=HTTPStatus.CREATED,
        )
