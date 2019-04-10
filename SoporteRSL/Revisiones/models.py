from django.db import models
from Investigadores import models

# Create your models here.

class PreguntaDeInvestigacion(models.Model):
    pregunta = models.CharField(max_length=150)
    revision = models.ForeignKey('Revision', on_delete=models.CASCADE)


class Revision(models.Model):
    meta_de_necesidad_de_informacion = models.Textfield()
    investigadores = models.ManyToManyField('Investigador',)
    cadena_de_busqueda = models.

