from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from trabajo_uci.models import Trabajo
from trabajo_uci.serializers import TrabajoSerializer
from users_uci.custom_permission import IsLoggedInAdminStudent, IsLoggedInAdminProfessor


# Create your views here.

class TrabajoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInAdminStudent]
    parser_classes = (MultiPartParser,)

    @staticmethod
    def post(request):
        if Trabajo.objects.filter(usuario_id=request.user.id, evento_id=request.data['evento']).exists():
            return Response({'message': 'El usuario registró un trabajo en el evento'},
                            status=HTTP_400_BAD_REQUEST)
        else:
            serializer = TrabajoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, slug_name):
        try:
            trabajo = Trabajo.objects.get(slug=slug_name)
            trabajo.delete()
            return Response({'message': 'Trabajo eliminado satisfactoriamente'}, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getTrabajoDetail(request, slug_name):
    try:
        trabajo = Trabajo.objects.get(slug=slug_name)
        serializer = TrabajoSerializer(trabajo, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([IsLoggedInAdminProfessor])
def getListTrabajo(request, slug_event):
    try:
        trabajos = Trabajo.objects.filter(evento__slug=slug_event)
        serializer = TrabajoSerializer(trabajos, many=True)
        return Response({'trabajos': serializer.data})
    except ObjectDoesNotExist:
        raise Http404
