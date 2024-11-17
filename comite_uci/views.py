from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from comite_uci.models import Comite
from comite_uci.serializers import ComiteSerializer
from users_uci.custom_permission import IsLoggedInAdminExceptions


# Create your views here.

class ComiteList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedInAdminExceptions]

    @staticmethod
    def post(request):
        if Comite.objects.filter(evento=request.data['evento']).exists():
            return Response({'message': 'El comité ya existe'}, status=HTTP_400_BAD_REQUEST)
        else:
            serializer = ComiteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, slug_name):
        try:
            comite = Comite.objects.get(slug=slug_name)
            serializer = ComiteSerializer(comite, data=request.data)
            if serializer.is_valid():
                serializer.save()
                comite.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise Http404

    @staticmethod
    def delete(request, slug_name):
        try:
            comite = Comite.objects.get(slug=slug_name)
            comite.delete()
            return Response({'message': 'Comité eliminado satisfactoriamente'}, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getComiteForEvent(request, slug_event):
    try:
        comites = Comite.objects.filter(evento__slug=slug_event)
        serializer = ComiteSerializer(comites, many=True)
        return Response({'comites': serializer.data}, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        raise Http404


@api_view(['GET'])
@permission_classes([AllowAny])
def getComiteDetail(request, slug_name):
    try:
        comite = Comite.objects.get(slug=slug_name)
        serializer = ComiteSerializer(comite, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        raise Http404
