from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users_uci.models import User
from users_uci.serializers import UserSerializer


# Create your views here.

class UserApi(APIView):
    permission_classes = ([AllowAny])
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
            if request.data['perfil'] == 'Profesor':
                context = {'id': serializer.data.get('id'), 'username': serializer.data.get('username'),
                           'first_name': serializer.data.get('first_name'), 'last_name': serializer.data.get('last_name'),
                           'email': serializer.data.get('email'), 'perfil': serializer.data.get('perfil'),
                           'category': serializer.data.get('category'),
                           'photo': str(serializer.data.get('photo'))}
                return Response(context, status=HTTP_201_CREATED)
            else:
                context = {'id': serializer.data.get('id'), 'username': serializer.data.get('username'),
                           'first_name': serializer.data.get('first_name'),
                           'last_name': serializer.data.get('last_name'),
                           'email': serializer.data.get('email'), 'perfil': serializer.data.get('perfil'),
                           'year_student': serializer.data.get('year_student'),
                           'photo': str(serializer.data.get('photo'))}
                return Response(context, status=HTTP_201_CREATED)
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
                       'email': user.email, 'perfil': user.perfil, 'category': user.category,
                       'photo': str(user.photo)}
            return Response(context, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, slug_username, format=None):
        user = self.get_object(slug_username)
        user.delete()
        return Response({'message': 'Usuario eliminado satisfactoriamente'}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def getSearchUser(request, username):
    try:
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
