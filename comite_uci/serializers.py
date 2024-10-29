from rest_framework import serializers

from comite_uci.models import Comite
from users_uci.serializers import UserSerializer


class ComiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comite
        fields = ['coordinador', 'miembros', 'evento', 'slug']
