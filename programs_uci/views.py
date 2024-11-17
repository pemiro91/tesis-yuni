from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from programs_uci.models import Programa
from programs_uci.serializers import ProgramaSerializer
from users_uci.custom_permission import IsLoggedInAdminExceptions


# Create your views here.

class ProgramsList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInAdminExceptions]

    @staticmethod
    def post(request):
        if Programa.objects.filter(nombre_programa=request.data['nombre_programa']).exists():
            return Response({'message': 'El programa ya existe'}, status=HTTP_400_BAD_REQUEST)
        else:
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
def getProgramsForEvent(request, slug_event):
    try:
        programs = Programa.objects.filter(evento__slug=slug_event)
        serializer = ProgramaSerializer(programs, many=True)
        return Response({'programas': serializer.data}, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getProgramDetail(request, slug_name):
    try:
        program = Programa.objects.get(slug=slug_name)
        serializer = ProgramaSerializer(program, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
