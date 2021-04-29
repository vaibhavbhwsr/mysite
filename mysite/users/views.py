from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import RegistrationForm


# Create your views here.


# Sign up

def sign_up(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/users/profile/')
	else:
	    form = RegistrationForm()
	    if request.method == 'POST':
	        form = RegistrationForm(request.POST)												# Yaha 1 parameter me kaam chal jaega
	        if form.is_valid():
	            form.save()
	            return render(request, 'users/msg.html', { 'message': "Succesfully Signed Up!",	})
	        else:
	            return render(request, 'users/signup.html', {'form': form})
	        
	    return render(request, 'users/signup.html', {'form': form})


# Log In

def log_in(request):
	if request.user.is_authenticated:															# This prevents users to get to login page using login in url
		return HttpResponseRedirect('/users/profile/')
	else:
		if request.method == 'POST':
			form = AuthenticationForm(request=request, data=request.POST)						# Isme 2 parameter dena jaruri h.
			if form.is_valid():
				username = form.request.POST['username']										# We can also use cleaned_data here
				password = form.cleaned_data['password']										# We can also use request.POST here
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					return HttpResponseRedirect('/users/profile/')
		else:
			form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})


# User Profile page

def profile_page(request):				
	if request.user.is_authenticated:														# is_authenticate function is used to check authenticity.	
		return render(request, 'users/profile.html', { 'name': request.user })				# It will send the username.
	else:																					# This prevents users to get to profile page using profile in url
		return HttpResponseRedirect('/users/login/')


# Log out

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/users/login/')