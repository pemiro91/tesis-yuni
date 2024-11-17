from rest_framework import serializers

from users_uci.models import User


# TODO:User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, )
    photo = serializers.ImageField(required=False)
    category = serializers.CharField(required=False)
    year_student = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'perfil', 'photo', 'category',
                  'year_student', 'slug']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
