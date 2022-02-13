from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from q_On_Fait.models import Q_On_Fait
from .serializers import  actionsSerializer
# Create your views here.

class qOnFaitList(APIView):

    def get(self, request):
        actions1 = Q_On_Fait.objects.all()
        serializer = actionsSerializer(actions1, many = True)
        return Response(serializer.data)

    def post(self):
        pass