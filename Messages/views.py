from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Messages.models import Message
from .serializers import  actionsSerializer
# Create your views here.

class MessageList(APIView):
    serializer_class  = actionsSerializer

    def get_queryset(self):
        Historiques = Message.objects.all()
        return Historiques

    def get(self, request):
        message1 = Message.objects.all()
        serializer = actionsSerializer(message1, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        historique_data = request.data

        new_histo = Message.objects.create(Email_Client=historique_data["Email_Client"], Message=historique_data[
            "Message"])

        new_histo.save()

        serializer = actionsSerializer(new_histo)

        return Response(serializer.data)