"""GestionAlumnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


from GarciaFutbolitis.views import inicio, cargar_inicio, cargar_vista_jugadores, crear_jugadores, detalle_jugadores, \
    editar_jugadores, \
    borrar_jugadores, cargar_vista_equipos, crear_equipos, detalle_equipos, editar_equipos, borrar_equipos

urlpatterns = [
    path('', inicio),
    path('GarciaFutbolitis/admin/', admin.site.urls),
    path('GarciaFutbolitis/inicio/', cargar_inicio),
    path('GarciaFutbolitis/equipos/', cargar_vista_equipos),
    path('GarciaFutbolitis/equipos/crear/', crear_equipos, name='crear_jugadores'),
    path('GarciaFutbolitis/equipos/<int:id>', detalle_equipos, name='detalle_jugadores'),
    path('GarciaFutbolitis/equipos/editar/<int:id>', editar_equipos, name='editar_jugadores'),
    path('GarciaFutbolitis/equipos/borrar/<int:id>', borrar_equipos, name='borrar_jugadores'),

    path('GarciaFutbolitis/jugadores/', cargar_vista_jugadores),
    path('GarciaFutbolitis/jugadores/crear/', crear_jugadores, name='crear_jugadores'),
    path('GarciaFutbolitis/jugadores/<int:id>',detalle_jugadores, name='detalle_jugadores'),
    path('GarciaFutbolitis/jugadores/editar/<int:id>', editar_jugadores, name='editar_jugadores'),
    path('GarciaFutbolitis/jugadores/borrar/<int:id>', borrar_jugadores, name='borrar_jugadores')
]
