from django.db import models
from django.db.models.fields import BigIntegerField

class Donation(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=500)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
        db_table = 'tipo_donacion'
        ordering= ['id']

class Document(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=500)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        db_table = 'tipo_documento'
        ordering= ['id']

class Pet(models.Model):
    name = models.CharField(verbose_name = 'Nombre de Mascota', max_length=100)
    pet_age = models.PositiveIntegerField(verbose_name='Edad')
    breed = models.CharField(verbose_name = 'Raza', max_length=100)
    description = models.TextField(verbose_name = 'Descripción', max_length=500)

    def __str__(self):
        return self.name
    
    class Meta:
	    verbose_name = 'Mascota'
	    verbose_name_plural = 'Mascotas'
	    db_table = 'mascota'
	    ordering = ['id']

class Adopcion(models.Model):
    name = models.CharField(verbose_name = 'Nombre de Mascota', max_length=100)
    pet_age = models.PositiveIntegerField(verbose_name='Edad')
    breed = models.CharField(verbose_name = 'Raza', max_length=100)
    user_name = models.CharField(verbose_name = 'Nombre de Usuario', max_length=100)
    nuDocument = models.PositiveBigIntegerField(verbose_name='Número de Documento')

    def __str__(self):
        return self.name
    
    class Meta:
	    verbose_name = 'Adopcion'
	    verbose_name_plural = 'Adopciones'
	    db_table = 'adopcion'
	    ordering = ['id']

class Solicitud(models.Model):
    name = models.CharField(max_length=40, verbose_name= 'Nombre')
    phone = models.IntegerField( verbose_name= 'Teléfono')
    email = models.EmailField(verbose_name= 'Email')
    nuDocument = models.IntegerField( verbose_name= 'No. de Documento')
    location = models.CharField(max_length=40, verbose_name= 'Localidad')
    Neighborhood = models.CharField(max_length=40, verbose_name= 'Barrio')
    address = models.CharField(max_length=40, verbose_name= 'Dirección')
    question = models.TextField(verbose_name = 'Alguna Pregunta')
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Solicitud'    
        verbose_name_plural = 'Solicitudes'
        db_table = 'solicitud_adopcion'
        ordering = ['id']

class User(models.Model):
    name = models.CharField (verbose_name='Nombres', max_length= 45)
    email = models.EmailField(verbose_name='Correo electronico')
    password = models.CharField(verbose_name='Contraseña', max_length=20)
    phone = models.IntegerField(verbose_name='Celular')
    birth = models.DateField(verbose_name='Fecha de nacimiento')
    no_document = models.BigIntegerField(verbose_name= 'No. de Documento')
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    solicitud_adopcion = models.ForeignKey(Solicitud, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table= 'usuario'
        ordering= ['id']
