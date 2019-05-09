from django.contrib import admin
from .models import *


class RevisionAdmin(admin.ModelAdmin):
    fields = ['titulo',
    'meta_de_necesidad_de_informacion',
    'investigadores',
    'cadena_de_busqueda',
    'metadatos',
    'bibliotecas',
    'prueba_piloto']

    
admin.site.register(Revision, RevisionAdmin)
admin.site.register(Biblioteca)
admin.site.register(Metadato)
admin.site.register(Criterio)
admin.site.register(PreguntaDeInvestigacion)
