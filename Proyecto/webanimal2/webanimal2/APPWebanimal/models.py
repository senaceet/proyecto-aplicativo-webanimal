from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(verbose_name = 'Nombre', max_length=100)
    email = models.EmailField(verbose_name= 'Email')
    phone = models.BigIntegerField( verbose_name= 'Teléfono')
    affair = models.TextField(verbose_name = 'Asunto', max_length=500)
    message = models.TextField(verbose_name = 'Mensaje', max_length=1000)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        db_table = 'contactos'
        ordering= ['id']

class Location(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'localidad'
        ordering= ['id']

class Neighborhood(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=100)
    localidad = models.ForeignKey(Location, on_delete=models.CASCADE)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        db_table = 'barrio'
        ordering= ['id']


class Document(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        db_table = 'tipo_documento'
        ordering= ['id']

class Questionnaire(models.Model):
    question1 = models.TextField(verbose_name = 'Descripción', max_length=500)
    question2 = models.TextField(verbose_name = 'Descripción', max_length=500)
    question3 = models.TextField(verbose_name = 'Descripción', max_length=500)
    question4 = models.TextField(verbose_name = 'Descripción', max_length=500)
    question5 = models.TextField(verbose_name = 'Descripción', max_length=500)

    def _str_(self):
        return self.question1

    class Meta:
        verbose_name = 'cuestionario'
        verbose_name_plural = 'cuestionarios'
        db_table = 'cuestionario'
        ordering= ['id']

class dog(models.Model):
    description = models.TextField(verbose_name = 'Descripción', max_length=500)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'raza perro'
        verbose_name_plural = 'razas perros'
        db_table = 'raza perros'
        ordering= ['id']

class cat(models.Model):
    description = models.TextField(verbose_name = 'Descripción', max_length=500)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'raza gato'
        verbose_name_plural = 'razas gatos'
        db_table = 'raza gatos'
        ordering= ['id']


class Breed(models.Model):
    description = models.TextField(verbose_name = 'Descripción', max_length=500)
    raza_perros = models.ForeignKey(dog, on_delete=models.CASCADE)
    raza_gatos = models.ForeignKey(cat, on_delete=models.CASCADE)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'raza'
        verbose_name_plural = 'razas'
        db_table = 'razas'
        ordering= ['id']

class Mascot(models.Model):
    name = models.CharField(verbose_name = 'Nombre de Mascota', max_length=100)
    pet_age = models.PositiveIntegerField(verbose_name='Edad')
    description = models.TextField(verbose_name = 'Descripción', max_length=500)
    razas = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        db_table = 'mascotas'
        ordering= ['id']

class User_register(models.Model):
    names = models.CharField(verbose_name='Nombres', max_length=100)
    document = models.BigIntegerField(verbose_name='No documento')
    Email = models.EmailField(verbose_name='Correo', max_length=100)
    password = models.CharField(verbose_name='Contraseña', max_length=100)
    telephone = models.BigIntegerField(verbose_name='Telefono')
    birth_date = models.DateField(verbose_name='Fecha nacimiento', max_length=50)
    direction = models.CharField(verbose_name='Direccion', max_length=50)
    tipo_documento = models.ForeignKey(Document, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'registro_usuario'
        ordering= ['id']

class Request_adoption(models.Model):
    message = models.TextField(verbose_name = 'mensaje', max_length=1000)
    registrousuario = models.ForeignKey(User_register, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascot, on_delete=models.CASCADE)
    

    def _str_(self):
        return self.message

    class Meta:
        verbose_name = 'solicitud adopcion'
        verbose_name_plural = 'solicitudes adopciones'
        db_table = 'solicitud_adopcion'
        ordering= ['id']

class Adoption(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=500)
    solicitud_adopcion  = models.ForeignKey(Request_adoption, on_delete=models.CASCADE)

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'Adopcion'
        verbose_name_plural = 'Adopciones'
        db_table = 'adopcion'
        ordering= ['id']

class Donation(models.Model):
    description = models.TextField(verbose_name='Descripción', max_length=500)
    registro_usuario = models.ForeignKey(User_register, on_delete=models.CASCADE)


    def _str_(self):
        return self.description

    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
        db_table = 'donaciones'
        ordering= ['id']