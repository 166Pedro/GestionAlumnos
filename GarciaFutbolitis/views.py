from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def cargar_inicio(request):
    return render(request, 'inicio.html')


def cargar_vista_equipos(requests):
    lista_equipos = Equipos.objects.all()
    return render(requests,'equipos.html', {'equipos': lista_equipos})  ##argumento, nombre template y diccionario devolviendo template renderizado

def crear_equipos(request):

    if request.method == 'POST':
        equipos = Equipos()
        equipos.id = request.POST.get('id')
        equipos.nombre = request.POST.get('nombre')
        equipos.save(equipos)
        return redirect('/GarciaFutbolitis/equipos/')
    else:
        return render(request, 'crear_equipos.html')

def editar_equipos(request,id):
    if request.method == "GET":
        equipos = Equipos.objects.get(id=id)
        return render(request, 'editar_equipos.html', {'equipos': equipos})
    else:
        equipos = Equipos()
        equipos.id = id
        equipos.nombre = request.POST.get('nombre')
        Equipos.save(equipos)
        return redirect('/GarciaFutbolitis/equipos/')

def detalle_equipos(request, id):
        equipos = Equipos.objects.get(id=id)
        context = {'equipos': equipos}
        return render(request, 'detalle_equipos.html', context)

def borrar_equipos(request, id):
        equipos = Equipos.objects.get(id=id)
        if equipos is not None:
            Equipos.delete(equipos)
        return redirect('/GarciaFutbolitis/equipos/')


########################################################################################################################


def cargar_vista_jugadores(requests):
    lista_jugadores = Jugadores.objects.all()
    return render(requests,'jugadores.html', {'jugadores': lista_jugadores})


def crear_jugadores(request):

    if request.method == 'POST':

        jugadores = Jugadores()
        jugadores.id = request.POST.get('id')
        jugadores.nombre = request.POST.get('nombre')
        jugadores.apellidos = request.POST.get('apellidos')
        jugadores.fecha_nacimiento = request.POST.get('fecha')
        jugadores.ranking = request.POST.get('ranking')
        variable1 = request.POST.get('equipo')
        jugadores.equipos = Equipos.objects.get(id=variable1)
        Jugadores.save(jugadores)
        return redirect('/GarciaFutbolitis/jugadores/')
    else:
        return render(request, 'crear_jugador.html')


def editar_jugadores(request,id):
    if request.method == "GET":
        jugadores = Jugadores.objects.get(id=id)
        return render(request, 'editar_jugadores.html', {'jugadores': jugadores})
    else:
        jugadores = Jugadores()
        jugadores.id = id
        jugadores.nombre = request.POST.get('nombre')
        jugadores.apellidos = request.POST.get('apellidos')
        jugadores.fecha_nacimiento = request.POST.get('nacimiento')
        jugadores.ranking = request.POST.get('ranking')
        variable = request.POST.get('equipo')
        jugadores.equipos = Equipos.objects.get(id=int(variable))
        Jugadores.save(jugadores)
        return redirect('/GarciaFutbolitis/jugadores/')



def detalle_jugadores(request, id):
    jugadores = Jugadores.objects.get(id=id)
    context = {'jugadores': jugadores}
    return render(request, 'jugadores_detalles.html', context)


def borrar_jugadores(request,id):
    jugadores = Jugadores.objects.get(id=id)
    if jugadores is not None:
        Jugadores.delete(jugadores)
    return redirect('/GarciaFutbolitis/jugadores/')