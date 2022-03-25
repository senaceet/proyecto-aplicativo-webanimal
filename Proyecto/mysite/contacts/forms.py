import email
from django import forms
from .models import Contacts


class ContactsForm(forms.Form):
    names = forms.CharField(label="Nombres y Apellidos", required=True, min_length=4, max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'names',
        'style': 'background-color: transparent; border: 1px solid black;',
    }))

    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'example@gmail.com',
        'style': 'background-color:transparent',
        'style': 'background-color: transparent; border: 1px solid black;',
    }))

    number = forms.IntegerField(label="Numero", required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'number',
        'style': 'background-color: transparent; border: 1px solid black;',
    }))

    issue = forms.CharField(label="Asunto a Tratar", required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'issue',
        'style': 'background-color: transparent; border: 1px solid black;',
    }))

    def save(self):
        return Contacts.objects.create(
            names = self.cleaned_data.get('names'),
            email = self.cleaned_data.get('email'),
            number = self.cleaned_data.get('number'),
            issue = self.cleaned_data.get('issue'),
        )
