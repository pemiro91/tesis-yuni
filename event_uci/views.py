from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
)
from rest_framework.views import APIView

from event_uci.models import Evento
from event_uci.serializers import EventoSerializer


# Create your views here.


class EventoList(APIView):
    permission_classes = ([AllowAny])

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
