import os

from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models

from eventos import settings

# Create your models here.


RESULTS = (
    ('Mención', 'Mención'),
    ('Destacado', 'Destacado'),
    ('Relevante', 'Relevante'),
)


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


class Comite(models.Model):
    coordinador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='coordinador')
    miembros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='miembros', blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.coordinador)
        super(Comite, self).save(*args, **kwargs)

    def __str__(self):
        return self.coordinador


class Trabajo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    documento = models.FileField(upload_to='trabajos/% Y/% m/% d/')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.usuario.username)
        super(Trabajo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.documento.path):
            os.remove(self.documento.path)

        super(Trabajo, self).delete(*args, **kwargs)

    def __str__(self):
        return self.usuario.username


class Resultado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    resultado_obtenido = models.CharField(max_length=20, choices=RESULTS)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.usuario.username)
        super(Resultado, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario.username


class Evidencia(models.Model):
    imagen = models.ImageField(upload_to='evidence/', null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento.nombre)
        super(Evidencia, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)

        super(Evidencia, self).delete(*args, **kwargs)

    def __str__(self):
        return self.evento.nombre


class Equipo(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    participantes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participantes', blank=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento.nombre)
        super(Equipo, self).save(*args, **kwargs)

    def __str__(self):
        return self.evento
