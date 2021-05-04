# This file is created one.
from django import forms                                                            # Imported forms 1st
from django.contrib.auth.models import User                                         # imported User 2nd
from django.contrib.auth.forms import UserCreationForm                              # imported UserCreationForm 3rd
 

class RegistrationForm(UserCreationForm):
    # This Meta tag class has been overridden here, already defined in UserCreationForm
    # Actually it Defines the top-bottom look of form fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'email' : 'Email'}                                                 # Used for changing label
