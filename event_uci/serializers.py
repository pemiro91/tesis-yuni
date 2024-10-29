from rest_framework import serializers

from event_uci.models import Evento


# TODO:Event Serializer
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'hora_inicio', 'contacto',
                  'ubicacion', 'slug']
