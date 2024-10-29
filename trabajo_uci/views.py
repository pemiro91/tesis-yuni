from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from trabajo_uci.models import Trabajo
from trabajo_uci.serializers import TrabajoSerializer


# Create your views here.

class TrabajoList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    @staticmethod
    def get(request):
        trabajos = Trabajo.objects.all()
        serializer = TrabajoSerializer(trabajos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = TrabajoSerializer(data=request.data)
        if serializer.is_valid():
            work = Trabajo.objects.filter(usuario_id=request.data['usuario'], evento=request.data['evento'])
            if work.exists():
                return Response({'message': 'El usuario registró un trabajo en el evento anteriormente'},
                                status=HTTP_403_FORBIDDEN)
            else:
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        try:
            trabajo = Trabajo.objects.get(slug=slug_name)
            serializer = TrabajoSerializer(trabajo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404

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
