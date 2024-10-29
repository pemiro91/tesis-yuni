from rest_framework import serializers

from equipo_uci.models import Equipo


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['evento', 'participantes', 'slug']
