from django import forms
from models import Revision

class NuevaRevision(forms.Form):
    template = 'nueva_revision.htm'
    model = Revision
    fields = ['titulo',
    'meta_de_necesidad_de_informacion',
    'investigadores',
    'cadena_de_busqueda',
    'metadatos',
    'bibliotecas',
    'prueba_piloto']