from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from eventos import settings


# Create your models here.


class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descripcion = models.TextField(name='descripcion')
    hora_inicio = models.TimeField(null=True, blank=True)
    contacto = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class ParticiparEvento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento.slug)
        super(ParticiparEvento, self).save(*args, **kwargs)

    def __str__(self):
        return self.evento.nombre
