from django.db import models

# Create your models here.

class Contacts(models.Model):
    names = models.CharField(verbose_name="Nombres", max_length=50)
    email = models.EmailField(verbose_name="Correo", unique=True)
    number = models.IntegerField(verbose_name="Numero")
    issue = models.TextField(verbose_name="Asunto", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.names
