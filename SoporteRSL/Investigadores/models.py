from django.db import models

# Create your models here.

class Investigador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)