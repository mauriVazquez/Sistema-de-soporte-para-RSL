from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Investigador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural="Investigadores"

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)