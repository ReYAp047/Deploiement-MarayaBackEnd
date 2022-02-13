from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Localisation.models import Localisation
from .serializers import  actionsSerializer
# Create your views here.

class localisationList(APIView):

    def get(self, request):
        actions1 = Localisation.objects.all()
        serializer = actionsSerializer(actions1, many = True)
        return Response(serializer.data)

    def post(self):
        pass