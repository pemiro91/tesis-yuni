from rest_framework import serializers

from event_uci.models import Evento
from eventos.validators import validate_result
from resultado_uci.models import Resultado
from trabajo_uci.models import Trabajo


class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    trabajo = serializers.PrimaryKeyRelatedField(queryset=Trabajo.objects.all())
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())
    resultado_obtenido = serializers.CharField(validators=[validate_result])

    class Meta:
        model = Resultado
        fields = ['trabajo', 'resultado_obtenido', 'evento', 'fecha', 'slug']


class GetResultadoSerializer(serializers.ModelSerializer):
    trabajo = serializers.PrimaryKeyRelatedField(queryset=Trabajo.objects.all())
    resultado_obtenido = serializers.CharField(validators=[validate_result])
    evento = serializers.SerializerMethodField()

    class Meta:
        model = Resultado
        fields = ['trabajo', 'resultado_obtenido', 'evento', 'fecha', 'slug']

    def get_evento(self, obj):
        # Retorna un diccionario con varios campos del modelo relacionado
        return {
            'id': obj.evento.id,
            'name': obj.evento.nombre,
            'description': obj.evento.descripcion,
            'slug': obj.evento.slug,
        }
