import os

from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings
from eventos.validators import validate_image_extension


# Create your models here.


class Evidencia(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    imagen = models.ImageField(upload_to='evidence/', null=True, blank=True, validators=[validate_image_extension])
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.usuario.username)
        super(Evidencia, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)

        super(Evidencia, self).delete(*args, **kwargs)

    def __str__(self):
        return self.evento.nombre
