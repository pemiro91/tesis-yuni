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


class GetParticiparEventoSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()
    evento = serializers.SerializerMethodField()

    class Meta:
        model = ParticiparEvento
        fields = ['id', 'usuario', 'evento', 'fecha', 'slug']

    def get_evento(self, obj):
        # Retorna un diccionario con varios campos del modelo relacionado
        return {
            'id': obj.evento.id,
            'name': obj.evento.nombre,
            'description': obj.evento.descripcion,
            'contacto': obj.evento.contacto,
            'ubicacion': obj.evento.ubicacion,
            'slug': obj.evento.slug,
        }

    def get_usuario(self, obj):
        # Retorna un diccionario con varios campos del modelo relacionado
        return {
            'id': obj.usuario.id,
            'username': obj.usuario.username,
            'first_name': obj.usuario.first_name,
            'last_name': obj.usuario.last_name,
        }
