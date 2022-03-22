from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=20,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'username',
        'placeholder' : 'username',
        'style': 'margin-bottom: 20px',
    }))
    email = forms.EmailField(required=True,
    widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'id' : 'email',
        'placeholder' : 'example@django.com',
        'style': 'margin-bottom: 20px',
    }))
    password = forms.CharField(label='Contraseña',required=True,
    widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : 'password',
        'style': 'margin-bottom: 20px',
    }))

    password2 = forms.CharField(label='Confirmar Contraseña', required=True,
    widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'style': 'margin-bottom: 20px',
    }))


    # Validacion de Username duplicado
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este username ya se encuentra en uso')

        return username

    # Validacion de email duplicado
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya se encuentra en uso')

        return email

    # Validacion de contraseñas
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')
    
    # Método save del registro
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
