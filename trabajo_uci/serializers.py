from rest_framework import serializers

from event_uci.models import Evento
from eventos.validators import validate_file_extension
from trabajo_uci.models import Trabajo
from users_uci.models import User


class TrabajoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
    evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())

    documento = serializers.FileField(validators=[validate_file_extension])

    class Meta:
        model = Trabajo
        fields = ['id', 'usuario', 'documento', 'evento', 'fecha', 'slug']
