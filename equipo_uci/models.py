from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings


# Create your models here.


class Equipo(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    participantes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participantes', blank=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento.nombre)
        super(Equipo, self).save(*args, **kwargs)

    def __str__(self):
        return self.evento
