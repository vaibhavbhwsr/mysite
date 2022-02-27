from django import forms
from group_chat.models import Group


class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
