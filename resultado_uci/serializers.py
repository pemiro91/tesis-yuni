from rest_framework import serializers

from event_uci.models import Evento
from eventos.validators import validate_result
from resultado_uci.models import Resultado
from users_uci.models import User


class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())
    resultado_obtenido = serializers.CharField(validators=[validate_result])

    class Meta:
        model = Resultado
        fields = ['usuario', 'resultado_obtenido', 'evento', 'fecha', 'slug']
