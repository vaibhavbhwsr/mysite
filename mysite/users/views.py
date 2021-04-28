from django.shortcuts import render
from django.http import HttpResponse											
from .forms import RegistrationForm	
from django.views.generic import CreateView, View																					

# Create your views here.

class IndexView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/signup.html/'
    success_url = 'success/'

class SuccessView(View):
    def get(self, request):
        return HttpResponse('Succesfully Signed Up!')