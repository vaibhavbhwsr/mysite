from django import forms

from group_chat.models import Group


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def clean(self):
        '''
        Changing spaces in name to underscore because URLs does not
        supports spaces.
        '''
        self.cleaned_data['name'] = self.cleaned_data['name'].replace(' ', '_')
