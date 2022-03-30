from django.contrib import admin
from .models import Adoption

# Register your models here.

class AdoptionAdmin(admin.ModelAdmin):
    fields = ('Nombres', 'Apellidos', 'number', 'Correo', 'Direccion', 'pregunta', 'pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5','state')
    list_display = ['__str__', 'created_at','state']
    list_filter = [ 'state', 'created_at' ]

admin.site.register(Adoption, AdoptionAdmin)