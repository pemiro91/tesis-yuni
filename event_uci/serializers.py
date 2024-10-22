from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from event_uci.models import User, Evento, Programa, Comite, Trabajo, Resultado, Evidencia, Equipo
from rest_framework import serializers


# TODO:User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, )
    photo = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'perfil', 'photo', 'slug']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# TODO:Event Serializer
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'hora_inicio', 'contacto',
                  'ubicacion', 'slug']


# TODO:Programs Serializer
class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())

    class Meta:
        model = Programa
        fields = ['nombre_programa', 'fecha', 'evento', 'slug']


class ComiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comite
        fields = ['coordinador', 'miembros', 'evento', 'slug']


class TrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajo
        fields = ['usuario', 'documento', 'evento', 'fecha', 'slug']


class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = ['usuario', 'resultado_obtenido', 'evento', 'fecha', 'slug']


class EvidenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evidencia
        fields = '__all__'


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
