from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'genai/index.html'


@method_decorator(login_required, name='dispatch')
class GenerateContentView(TemplateView):
    template_name = 'genai/content/index.html'
