from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from evidencia_uci.models import Evidencia
from evidencia_uci.serializers import EvidenciaSerializer, GetEvidenciaSerializer
from users_uci.custom_permission import IsLoggedInStudent, IsLoggedInAll


# Create your views here.

class EvidenciaList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInStudent]

    @staticmethod
    def get(request):
        evidence = Evidencia.objects.all()
        serializer = EvidenciaSerializer(evidence, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = EvidenciaSerializer(data=request.data)
        if serializer.is_valid():
            evidence = Evidencia.objects.filter(usuario_id=request.data['usuario'], evento=request.data['evento'])
            if evidence.exists():
                return Response({'message': 'El usuario ya tiene una evidencia registrada en el evento'},
                                status=HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        try:
            evidence = Evidencia.objects.get(slug=slug_name)
            serializer = EvidenciaSerializer(evidence, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404

    @staticmethod
    def delete(request, slug_name):
        try:
            evidence = Evidencia.objects.get(slug=slug_name)
            evidence.delete()
            return Response({'message': 'Evidencia eliminada satisfactoriamente'}, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getEvidenciaDetail(request, slug_name):
    try:
        evidencia = Evidencia.objects.get(slug=slug_name)
        serializer = GetEvidenciaSerializer(evidencia, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([IsLoggedInAll])
def getEvidenciasForUser(request):
    try:
        evidencias = Evidencia.objects.filter(usuario_id=request.user.id)
        serializer = GetEvidenciaSerializer(evidencias, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
