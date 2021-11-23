from django import forms
from django.forms import widgets

from .models import User_register

class User_registerMio(forms.ModelForm):
    class Meta: 
        model = User_register
        fields = '__all__'
        widgets = {'birth_date': forms.DateInput(attrs={'type':'date'})}