from django.db import models

# Create your models here.
class Adoption(models.Model):
    Nombres = models.CharField(verbose_name="Nombres", max_length=50)
    Apellidos = models.CharField(verbose_name="Apellidos", max_length=50) 
    number = models.IntegerField(verbose_name="Numero", max_length=20)
    Correo = models.EmailField(verbose_name="Correo",unique=True, max_length=500)
    Direccion = models.CharField(verbose_name="Direccion", max_length=20)
    pregunta = models.CharField(verbose_name="pregunta", max_length=500)
    pregunta1 = models.CharField(verbose_name="pregunta", max_length=500)
    pregunta2 = models.CharField(verbose_name="pregunta", max_length=500)
    pregunta3 = models.CharField(verbose_name="pregunta", max_length=500)
    pregunta4 = models.CharField(verbose_name="pregunta", max_length=500)
    pregunta5 = models.CharField(verbose_name="pregunta", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names