from django.db import models
from django.contrib.auth.models import User
import datetime


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} | {self.comision}"


class Noticias(models.Model):
    titular = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=4000)
    categoria = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="noticias", null=True, blank=True)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return f"{self.titular} | {self.autor}"


class Estudiante(models.Model):
    nombre = models.CharField(
        max_length=256,
    )
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} | {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    dni = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre} | {self.apellido}"

    bio = models.TextField()


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} | {self.aprobado}"
