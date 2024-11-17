from rest_framework import serializers

from event_uci.models import Evento, ParticiparEvento


# TODO:Event Serializer
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'hora_inicio', 'contacto',
                  'ubicacion', 'slug']


class ParticiparEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticiparEvento
        fields = ['id', 'usuario', 'evento', 'fecha', 'slug']
        depth = 1
