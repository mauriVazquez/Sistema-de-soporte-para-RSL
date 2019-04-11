from django.db import models
from Investigadores import models

# Create your models here.

class PreguntaDeInvestigacion(models.Model):
    pregunta = models.CharField(max_length=150)
    revision = models.ForeignKey('Revision', on_delete=models.CASCADE)


class Metadato(models.Model):
    nombre = models.CharField(max_length=50)


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)


class Criterio(models.Model):

    TIPO_DE_CRITERIO_CHOICE=(
        ('IN', 'inclusion'),
        ('EX', 'exclusion'),
        ('CA', 'calidad')
    )

    tipo = models.CharField(max_length=2, choices=TIPO_DE_CRITERIO_CHOICE, default='inclusion')
    descripcion = models.CharField(max_length=200)
    revison = models.ForeignKey("Revision", on_delete=models.CASCADE)


class Revision(models.Model):
    meta_de_necesidad_de_informacion = models.Textfield()
    investigadores = models.ManyToManyField('Investigador')
    cadena_de_busqueda = models.Charfield(max_length=200,)
    metadatos = models.ManyToManyField("Metadato")
    bibliotecas = models.ManyToManyField("Biblioteca")
    prueba_piloto = models.BooleanField(default=False)