from django.db import models
from Investigadores.models import Investigador

# Create your models here.

class PreguntaDeInvestigacion(models.Model):
    pregunta = models.CharField(max_length=150)
    revision = models.ForeignKey('Revision', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="preguntas de investigacion" 


class Metadato(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="metadatos" 

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="bibliotecas"

class Criterio(models.Model):

    TIPO_DE_CRITERIO_CHOICE=(
        ('IN', 'inclusion'),
        ('EX', 'exclusion'),
        ('CA', 'calidad')
    )

    tipo = models.CharField(max_length=2, choices=TIPO_DE_CRITERIO_CHOICE, default='inclusion')
    descripcion = models.CharField(max_length=200)
    revison = models.ForeignKey("Revision", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Criterios"


class Revision(models.Model):
    meta_de_necesidad_de_informacion = models.CharField(max_length=500)
    investigadores = models.ManyToManyField('Investigadores.Investigador')
    cadena_de_busqueda = models.CharField(max_length=200,)
    metadatos = models.ManyToManyField("Metadato")
    bibliotecas = models.ManyToManyField("Biblioteca")
    prueba_piloto = models.BooleanField(default=False, verbose_name= "¿Se realizara prueba piloto?")
    fecha_inicio = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="revisiones"