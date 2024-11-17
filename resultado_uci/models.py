from django.db import models
from django.utils.text import slugify

from event_uci.models import Evento
from eventos import settings
from eventos.validators import validate_result
from trabajo_uci.models import Trabajo

# Create your models here.

RESULTS = (
    ('Mención', 'Mención'),
    ('Destacado', 'Destacado'),
    ('Relevante', 'Relevante'),
)


class Resultado(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, name='trabajo')
    resultado_obtenido = models.CharField(max_length=20, choices=RESULTS, validators=[validate_result])
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, name='evento')
    fecha = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.trabajo.slug)
        super(Resultado, self).save(*args, **kwargs)

    def __str__(self):
        return self.resultado_obtenido
