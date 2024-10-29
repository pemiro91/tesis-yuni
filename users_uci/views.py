from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users_uci.models import User
from users_uci.serializers import UserSerializer


# Create your views here.

class UserApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def get_object(slug_username):
        try:
            return User.objects.get(slug=slug_username)
        except User.DoesNotExist:
            raise Http404

    @staticmethod
    def get(request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_username, format=None):
        user = User.objects.get(slug=slug_username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user.set_password(request.data.get("password"))
            user.save()
            context = {'id': user.id, 'username': user.username,
                       'first_name': user.first_name, 'last_name': user.last_name,
                       'email': user.email, 'perfil': user.perfil, 'photo': str(user.photo)}
            return Response(context, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, slug_username, format=None):
        user = self.get_object(slug_username)
        user.delete()
        return Response({'message': 'Usuario eliminado satisfactoriamente'}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
