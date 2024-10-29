from rest_framework import serializers

from event_uci.models import Evento
from eventos.validators import validate_image_extension
from evidencia_uci.models import Evidencia
from users_uci.models import User


class EvidenciaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())
    imagen = serializers.ImageField(required=True, validators=[validate_image_extension])

    class Meta:
        model = Evidencia
        fields = ['usuario', 'evento', 'imagen', 'fecha', 'slug']
