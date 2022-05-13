from django.db import models


class Equipos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


# Create your models here.
class Jugadores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)
    apellidos = models.TextField(max_length=150)
    fecha_nacimiento = models.DateField()
    ranking = models.IntegerField()
    equipos = models.ForeignKey(Equipos, on_delete=models.CASCADE, default=None)

    def __str__(self):  ##objetos mostrados como cadena
        return self.nombre, self.apellidos, self.fecha_nacimiento, self.ranking  ##pasamos valor a los atributos de la instancia
