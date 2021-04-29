# This file is created one.
from django import forms                                                            # Imported forms 1st
from django.contrib.auth.models import User                                         # imported User 2nd
from django.contrib.auth.forms import UserCreationForm                              # imported UserCreationForm 3rd
 

# This class inherits properties of UserCreationForm class declared above
class RegistrationForm(UserCreationForm):

    #password2 declared here is just to customize it from forms
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    # This Meta tag class has been overridden here, already defined in UserCreationForm
    # Actually it Defines the top-bottom look of form fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'email' : 'Email'}                                                 # Used for changing label
