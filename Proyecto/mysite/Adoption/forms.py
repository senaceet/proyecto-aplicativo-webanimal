from django import forms
# from django.contrib.auth.models import User
from .models import Adoption

class AdoptionForm(forms.Form):
    Nombres = forms.CharField(required=True, max_length=20,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'Nombres',
        'placeholder' : 'Nombres',
        'style': 'margin-bottom: 20px',
    }))
    Apellidos = forms.CharField(required=True, max_length=100,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'Apellidos',
        'placeholder' : 'Apellidos',
        'style': 'margin-bottom: 20px',
    }))
    number = forms.IntegerField(required=True,
    widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'id' : 'Telefono',
        'placeholder' : 'Telefono',
        'style': 'margin-bottom: 20px',
    }))
    Correo= forms.EmailField(required=True, max_length=70,
    widget=forms.TextInput(attrs={
        'name': 'Correo',
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Correo',
        'style': 'margin-bottom: 10px',
    }))
    Direccion = forms.CharField(required=True, max_length=20,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'Direccion',
        'placeholder' : 'Direccion',
        'style': 'margin-bottom: 20px',
    }))
    pregunta = forms.CharField(label="Ocupación", required=True, max_length=60,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))

    pregunta1 = forms.CharField(label="¿Por que desea adoptar?", required=True, min_length=20, max_length=100,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))
    pregunta2 = forms.CharField(label="¿Vives en casa o departamento?, Si es departamento, ¿permiten mascotas en el edificio?", required=True, min_length=20, max_length=500,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))
    pregunta3 = forms.CharField(label="¿Tu vivienda es propia o alquilada?, Si es alquilada, ¿Tienes permiso del dueño?, ¿Qué harías si tuvieras que mudarte?", required=True, min_length=20, max_length=500,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))
    pregunta4 = forms.CharField(label="¿Es un lugar seguro para una mascota?, ¿Tienes rejas o cercas que impidan que tu mascota escape o que se la roben?", required=True, min_length=20, max_length=500,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))
    pregunta5 = forms.CharField(label="¿Tienes espacio suficiente para una mascota?, ¿A qué áreas de tu hogar tendrá acceso?", required=True, min_length=20, max_length=500,
    widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'Correo',
        'placeholder' : 'Tu Respuesta',
        'style': 'margin-bottom: 10px',
    }))
    # pregunta1 = forms.CharField(label="¿Por que desea adoptarla?", required=True, min_length=20, max_length=500,
    # widget=forms.TextInput(attrs={
    #     'class' : 'form-control',
    #     'id' : 'Correo',
    #     'placeholder' : 'Correo',
    #     'style': 'margin-bottom: 10px',
    # }))

    

    def save(self):
        return Adoption.objects.create(
            Nombres = self.cleaned_data.get('Nombres'),
            Apellidos = self.cleaned_data.get('Apellidos'),
            number = self.cleaned_data.get('number'),
            Correo = self.cleaned_data.get('Correo'),
            Direccion = self.cleaned_data.get('Direccion'),
            pregunta = self.cleaned_data.get('pregunta'),
            pregunta1 = self.cleaned_data.get('pregunta1'),
            pregunta2 = self.cleaned_data.get('pregunta2'),
            pregunta3 = self.cleaned_data.get('pregunta3'),
            pregunta4 = self.cleaned_data.get('pregunta4'),
            pregunta5 = self.cleaned_data.get('pregunta5'),
        )