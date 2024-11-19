from django.utils.timezone import now

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED, HTTP_200_OK
)
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from event_uci.models import Evento, ParticiparEvento
from event_uci.serializers import EventoSerializer, ParticiparEventoSerializer
from users_uci.custom_permission import IsLoggedInAdmin, IsLoggedInAll, IsLoggedInStudent, IsLoggedInAdminProfessor


# Create your views here.


class EventoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInAdmin]

    @staticmethod
    def get(request):
        events = Evento.objects.all()
        serializer = EventoSerializer(events, many=True)
        return Response({'eventos': serializer.data}, status=HTTP_200_OK)

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
    try:
        event = Evento.objects.get(slug=slug_name)
        serializer = EventoSerializer(event, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getEventForName(request, name):
    try:
        events = Evento.objects.filter(nombre__contains=name)
        serializer = EventoSerializer(events, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404


class ParticiparEventoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInStudent]

    @staticmethod
    def post(request):
        if ParticiparEvento.objects.filter(evento_id=request.data['evento'],
                                           usuario_id=request.data['usuario']).exists():
            return Response({'message': 'El estudiante ya participó en el evento'}, status=HTTP_400_BAD_REQUEST)
        else:
            serializer = ParticiparEventoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, slug_name):
        event = Evento.objects.get(slug=slug_name)
        event.delete()
        return Response({'message': 'Evento eliminado satisfactoriamente'}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsLoggedInAdminProfessor])
def getUsersForEvent(request, slug_name):
    try:
        event = ParticiparEvento.objects.filter(evento__slug=slug_name)
        serializer = ParticiparEventoSerializer(event, many=True)
        return Response({'users_event': serializer.data})
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getEventsForNext(request):
    try:
        event = Evento.objects.filter(fecha_inicio__gte=now())
        serializer = EventoSerializer(event, many=True)
        return Response({'events_next': serializer.data})
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getEventsForMonth(request):
    try:
        year_now = now().year
        month_now = now().month
        events = Evento.objects.filter(fecha_inicio__year=year_now, fecha_inicio__month=month_now)
        serializer = EventoSerializer(events, many=True)
        return Response({'events_month': serializer.data})
    except ObjectDoesNotExist:
        raise Http404
