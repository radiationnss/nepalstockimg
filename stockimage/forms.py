from dataclasses import fields
from email.mime import image
from django import forms
from .models import Image

class AddImageForm(forms.ModelForm):
    class Meta:
        model   = Image
        fields  = ['title', 'description', 'image', 'price', 'uploaded_by']

