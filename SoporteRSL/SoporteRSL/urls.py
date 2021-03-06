"""SoporteRSL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .utils import redireccionar
from Investigadores.views import inicio
from Revisiones.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', redireccionar),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.auth_logout, name='logout'),
    path('inicio/', inicio, name='inicio'),
    #path('revisiones/nueva_revision', RevisionCreateView.as_view(), name='revision_add'),
    path('revisiones/comenzar_revision', comenzar_revision , name='comenzar-revision'),
    path('revisiones/nueva_revision', nueva_revision , name='nueva-revision'),
    path('revisiones/<int:revision_id>/', detalle, name='detalle'),
    path('crear_formulario/<int:revision_id>/', crear_formulario, name='crear-formulario'),
    path('ayuda/', ayuda, name='ayuda'),
    path('ayuda/actividad_1',actividad_1, name='actividad-1'),
    path('ayuda/actividad_2',actividad_2, name='actividad-2'),
    path('ayuda/actividad_3',actividad_3, name='actividad-3'),
]
