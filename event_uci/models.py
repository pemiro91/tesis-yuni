from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


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
