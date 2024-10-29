from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings
from eventos.validators import validate_result

# Create your models here.

RESULTS = (
    ('Mención', 'Mención'),
    ('Destacado', 'Destacado'),
    ('Relevante', 'Relevante'),
)


class Resultado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='usuario')
    resultado_obtenido = models.CharField(max_length=20, choices=RESULTS, validators=[validate_result])
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.usuario.username)
        super(Resultado, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario.username
