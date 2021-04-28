from django.shortcuts import render
from django.http import HttpResponse  # Added
from .forms import RegistrationForm  # Added
# from django.contrib import messages  # Added
from django.views.generic.edit import CreateView


# Create your views here.

def sign_up(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Succefully Signed up! </h1>')
        else:
            form = RegistrationForm()
        return render(request, 'users/signup.html', {'form': form})
    return render(request, 'users/signup.html', {'form': form})

# for messages commented above to be displayed you have to let them print 
# on every page and defined their scope on base.html of whole site.

##########################