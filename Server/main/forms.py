from dataclasses import field
from django import forms
from .models import *


class NewImageForm(forms.ModelForm):
    class Meta:
        model = UserImages
        fields = ['image']
        