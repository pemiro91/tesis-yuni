from rest_framework import serializers

from event_uci.models import Evento
from programs_uci.models import Programa


# TODO:Programs Serializer
class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())

    class Meta:
        model = Programa
        fields = ['nombre_programa', 'fecha', 'evento', 'slug']
