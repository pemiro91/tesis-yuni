from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento


# Create your models here.

class Programa(models.Model):
    nombre_programa = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_programa)
        super(Programa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_programa
