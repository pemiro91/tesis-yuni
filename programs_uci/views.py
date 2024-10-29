from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from programs_uci.models import Programa
from programs_uci.serializers import ProgramaSerializer


# Create your views here.

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
    try:
        program = Programa.objects.get(slug=slug_name)
        serializer = ProgramaSerializer(program, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404

