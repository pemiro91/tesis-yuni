# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from resultado_uci.models import Resultado
from resultado_uci.serializers import ResultadoSerializer, GetResultadoSerializer
from users_uci.custom_permission import IsLoggedInAdminProfessor, IsLoggedInStudent


class ResultadoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInAdminProfessor]

    @staticmethod
    def get(request):
        results = Resultado.objects.all()
        serializer = ResultadoSerializer(results, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        if Resultado.objects.filter(evento=request.data['evento'], trabajo=request.data['trabajo']).exists():
            return Response({'message': 'El trabajo ya tiene un resultado asignado'}, status=HTTP_400_BAD_REQUEST)
        else:
            serializer = ResultadoSerializer(data=request.data)
            if serializer.is_valid():
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
@permission_classes([IsLoggedInAdminProfessor])
def getListResultadoForEvent(request, slug_event):
    try:
        result = Resultado.objects.filter(evento__slug=slug_event)
        serializer = ResultadoSerializer(result, many=True)
        return Response({'resultados': serializer.data})
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsLoggedInStudent])
def getListResultsForStudent(request):
    try:
        result = Resultado.objects.filter(trabajo__usuario_id=request.user.id)
        serializer = GetResultadoSerializer(result, many=True)
        return Response({'resultados': serializer.data})
    except ObjectDoesNotExist:
        raise Http404
