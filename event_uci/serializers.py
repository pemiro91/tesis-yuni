from rest_framework import serializers

from event_uci.models import Evento, Comite, Trabajo, Resultado, Evidencia, Equipo


# TODO:Event Serializer
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'hora_inicio', 'contacto',
                  'ubicacion', 'slug']


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
