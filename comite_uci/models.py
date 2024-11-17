from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings


# Create your models here.

class Comite(models.Model):
    coordinador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='coordinador')
    miembros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='miembros', blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento.slug)
        super(Comite, self).save(*args, **kwargs)

    def __str__(self):
        return self.coordinador
