import os

from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings
from eventos.validators import validate_file_extension


# Create your models here.

class Trabajo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    documento = models.FileField(upload_to='trabajos/%Y/%m/%d/', validators=[validate_file_extension])
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
