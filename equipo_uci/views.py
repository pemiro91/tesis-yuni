from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

from equipo_uci.models import Equipo
from equipo_uci.serializers import EquipoSerializer


# Create your views here.

class EquipoList(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        try:
            equipo = Equipo.objects.get(slug=slug_name)
            serializer = EquipoSerializer(equipo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404

    @staticmethod
    def delete(request, slug_name):
        try:
            equipo = Equipo.objects.get(slug=slug_name)
            equipo.delete()
            return Response({'message': 'Equipo eliminado satisfactoriamente'}, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getEquipoDetail(request, slug_name):
    try:
        equipo = Equipo.objects.get(slug=slug_name)
        serializer = EquipoSerializer(equipo, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
