from django import forms

from .models import Trash

class TrashForm(forms.ModelForm):
    class Meta:
        model = Trash
        fields = ['trash_description']
        label = {'trash_description':''}