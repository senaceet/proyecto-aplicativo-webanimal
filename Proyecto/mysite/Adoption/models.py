from django.db import models

# Create your models here.
class Adoption(models.Model):
    Nombres = models.CharField(verbose_name="Nombres", max_length=50)
    Apellidos = models.CharField(verbose_name="Apellidos", max_length=60) 
    number = models.IntegerField(verbose_name="Numero")
    Correo = models.EmailField(verbose_name="Correo",unique=True, max_length=500)
    Direccion = models.CharField(verbose_name="Direccion", max_length=20)
    pregunta = models.TextField(verbose_name="pregunta", max_length=60)
    pregunta1 = models.TextField(verbose_name="pregunta", max_length=100)
    pregunta2 = models.TextField(verbose_name="pregunta", max_length=100)
    pregunta3 = models.TextField(verbose_name="pregunta", max_length=100)
    pregunta4 = models.TextField(verbose_name="pregunta", max_length=100)
    pregunta5 = models.TextField(verbose_name="pregunta", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombres