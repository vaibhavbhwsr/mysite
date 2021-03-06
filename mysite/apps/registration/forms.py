# This file is created one.
from django import forms
# imported UserCreationForm 3rd
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # imported User 2nd


# This class inherits properties of UserCreationForm class declared above
class RegistrationForm(UserCreationForm):
    # This Meta tag class has been overridden here, already defined
    # In UserCreationForm
    # Actually it Defines the top-bottom look of form fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # Used for changing label
        labels = {'email': 'Email', 'password2': 'Confirm Password'}
