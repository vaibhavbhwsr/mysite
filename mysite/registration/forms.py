# This file is created one.
from django import forms
from django.contrib.auth.models import User  # imported User 2nd
from django.contrib.auth.forms import UserCreationForm  # imported UserCreationForm 3rd
from .models import Post


# This class inherits properties of UserCreationForm class declared above
class RegistrationForm(UserCreationForm):
    # This Meta tag class has been overridden here, already defined in UserCreationForm
    # Actually it Defines the top-bottom look of form fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email', 'password2': 'Confirm Password'}  # Used for changing label


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'picture', 'tags']
