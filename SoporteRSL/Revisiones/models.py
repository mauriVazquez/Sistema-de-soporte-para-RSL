from django.db import models
from Investigadores.models import Investigador

# Create your models here.

class PreguntaDeInvestigacion(models.Model):
    pregunta = models.CharField(max_length=150)
    revision = models.ForeignKey('Revision', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="preguntas de investigacion" 

    def __str__(self):
        return '%s -- %s' % (self.pregunta,self.revision) 

class Metadato(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="metadatos"

    def __str__(self):
        return '%s' % (self.nombre) 


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="bibliotecas"

    def __str__(self):
        return '%s' % (self.nombre)


class Criterio(models.Model):

    TIPO_DE_CRITERIO_CHOICE=(
        ('IN', 'inclusion'),
        ('EX', 'exclusion'),
        ('CA', 'calidad')
    )

    tipo = models.CharField(max_length=2, choices=TIPO_DE_CRITERIO_CHOICE, default='inclusion')
    descripcion = models.CharField(max_length=200)
    revision = models.ForeignKey("Revision", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Criterios"

    def __str__(self):
        return '%s - %s' % (self.tipo, self.descripcion)


class Articulo(models.Model):
    titulo = models.CharField(max_length= 50)
    revision = models.ForeignKey("Revision", on_delete=models.CASCADE)
    leido = models.BooleanField(default=False , verbose_name="¿El articulo fue leeido?" )
    archivo = models.FileField(upload_to="articulos/")
    formulario_de_extraccion = models.FileField(upload_to="formularios_de_extraccion/")

    class Meta:
        verbose_name_plural = "Articulos"

    def __str__(self):
        return '%s' % (self.titulo)

class Modificacion(models.Model):
    revision = models.ForeignKey("Revision", on_delete=models.CASCADE)
    investigador = models.ForeignKey('Investigadores.Investigador', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Modificaciones"

    def __str__(self):
        return 'Modificacion - %s - revision - %s' % (self.fecha,self.revision)

class Revision(models.Model):
    ESTADO_CHOICE=(
        ('A1', 'Actividad 1'),
        ('A2', 'Actividad 2'),
        ('A3', 'Actividad 3')
    )

    titulo = models.CharField(max_length=80)
    meta_de_necesidad_de_informacion = models.CharField(max_length=500)
    investigadores = models.ManyToManyField('Investigadores.Investigador', verbose_name= "Investigadores")
    cadena_de_busqueda = models.CharField(max_length=200,)
    metadatos = models.ManyToManyField("Metadato")
    bibliotecas = models.ManyToManyField("Biblioteca")
    prueba_piloto = models.BooleanField(default=False, verbose_name= "¿Se realizara prueba piloto?")
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICE, default='Actividad 1')
    fecha_inicio = models.DateField(auto_now_add=True)
    formulario_generico = models.BooleanField(default=False, verbose_name= "¿Se creo un formulario de extraccion de datos?")
    class Meta:
        verbose_name_plural="revisiones"

    def __str__(self):
        return '%s' % (self.titulo)

