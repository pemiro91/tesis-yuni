from rest_framework import serializers

from event_uci.models import Evento, ParticiparEvento
from users_uci.serializers import UserSerializer


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

    def to_representation(self, instance):
        self.fields['usuario'] = UserSerializer(read_only=True)
        self.fields['evento'] = EventoSerializer(read_only=True)
        return super(ParticiparEventoSerializer, self).to_representation(instance)

