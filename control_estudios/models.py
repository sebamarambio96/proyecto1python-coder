from django.db import models
from django.utils import timezone

class Noticias(models.Model):
    titular = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=4000)
    categoria = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="noticias", null=True, blank=True)
    fecha_publicacion = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.titular} | {self.autor}"