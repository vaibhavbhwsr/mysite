# This file is created one.
from django import forms  # noqa: F401
# imported UserCreationForm 3rd
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  # imported User 2nd

User = get_user_model()


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
