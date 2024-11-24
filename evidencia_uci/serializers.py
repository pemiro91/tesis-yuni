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


class GetEvidenciaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SerializerMethodField()
    evento = serializers.SerializerMethodField()
    imagen = serializers.ImageField(required=True, validators=[validate_image_extension])

    class Meta:
        model = Evidencia
        fields = ['usuario', 'evento', 'imagen', 'fecha', 'slug']

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
