# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from resultado_uci.models import Resultado
from resultado_uci.serializers import ResultadoSerializer


class ResultadoList(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        results = Resultado.objects.all()
        serializer = ResultadoSerializer(results, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = ResultadoSerializer(data=request.data)
        if serializer.is_valid():
            result = Resultado.objects.filter(usuario_id=request.data['usuario'], evento=request.data['evento'])
            if result.exists():
                return Response({'message': 'El usuario ya tiene un resultado asignado'},
                                status=HTTP_403_FORBIDDEN)
            else:
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        try:
            result = Resultado.objects.get(slug=slug_name)
            serializer = ResultadoSerializer(result, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404

    @staticmethod
    def delete(request, slug_name):
        try:
            result = Resultado.objects.get(slug=slug_name)
            result.delete()
            return Response({'message': 'Resultado eliminado satisfactoriamente'}, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getResultadoDetail(request, slug_name):
    try:
        result = Resultado.objects.get(slug=slug_name)
        serializer = ResultadoSerializer(result, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
