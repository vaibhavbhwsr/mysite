from django import forms

from group_chat.models import Group
from django.core.exceptions import ValidationError
import re



class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def clean_name(self):
        '''
        Changing spaces in name to underscore because URLs does not
        supports spaces.
        '''
        if not re.fullmatch('[A-Za-z0-9_.-]*', self.cleaned_data['name']):
            raise ValidationError(
                    "Only ASCII alphanumerics, hyphens, underscores, periods and less than "
                    "100 characters without space are allowed."
                )

        return self.cleaned_data['name']
