from django.contrib.auth import authenticate
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_200_OK
)
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from event_uci.models import Evento, User, Programa
from event_uci.serializers import UserSerializer, EventoSerializer, ProgramaSerializer


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
            return Response({serializer.data}, status=HTTP_201_CREATED)
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
                       'email': user.email, 'perfil': user.perfil, 'photo': user.photo}
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


class EventoList(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        events = Evento.objects.all()
        serializer = EventoSerializer(events, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request, format=None):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        event = Evento.objects.get(slug=slug_name)
        serializer = EventoSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            event.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, slug_name):
        event = Evento.objects.get(slug=slug_name)
        event.delete()
        return Response({'message': 'Evento eliminado satisfactoriamente'}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getEventDetail(request, slug_name):
    event = Evento.objects.get(slug=slug_name)
    serializer = EventoSerializer(event, many=False)
    return Response(serializer.data)


class ProgramsList(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):

        programs = Programa.objects.all()
        serializer = ProgramaSerializer(programs, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = ProgramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        program = Programa.objects.get(slug=slug_name)
        serializer = ProgramaSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            program.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, slug_name):
        program = Programa.objects.get(slug=slug_name)
        program.delete()
        return Response({'message': 'Programa eliminado satisfactoriamente'}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getProgramDetail(request, slug_name):
    program = Programa.objects.get(slug=slug_name)
    serializer = ProgramaSerializer(program, many=False)
    return Response(serializer.data)
