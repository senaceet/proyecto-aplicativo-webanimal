import email
from django import forms
from .models import Contacts


class ContactsForm(forms.Form):
    names = forms.CharField(label="Nombres y Apellidos", required=True, min_length=4, max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'names',
    }))

    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'example@gmail.com',
    }))

    number = forms.IntegerField(label="Numero", required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'number',
    }))

    issue = forms.CharField(label="Asunto a tratar", required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'issue',
    }))

    def save(self):
        return Contacts.objects.create(
            names = self.cleaned_data.get('names'),
            email = self.cleaned_data.get('email'),
            number = self.cleaned_data.get('number'),
            issue = self.cleaned_data.get('issue'),
        )