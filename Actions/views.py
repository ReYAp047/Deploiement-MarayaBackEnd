from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Actions.models import Actions
from Actions.models import Images
from Actions.models import FontImages
from Actions.models import Partonaire
from Actions.models import Videos

from .serializers import  actionsSerializer
from .serializers import  imagesSerializer
from .serializers import  fontImagesSerializer
from .serializers import  partonairesSerializer
from .serializers import  videosSerializer
# Create your views here.

class actionsList(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                action = Actions.objects.get(id=id)
                serializer = actionsSerializer(action)       
        except:
            actions1 = Actions.objects.all()
            serializer = actionsSerializer(actions1, many = True)

        return Response(serializer.data)

    def post(self):
        pass

class imagesList(APIView):
    
    def get(self, request):
        images1 = Images.objects.all()
        serializer = imagesSerializer(images1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class fontImagesList(APIView):
    
    def get(self, request):
        fontImages1 = FontImages.objects.all()
        serializer = fontImagesSerializer(fontImages1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class partonairesList(APIView):
    
    def get(self, request):
        partonaires1 = Partonaire.objects.all()
        serializer = partonairesSerializer(partonaires1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class videosList(APIView):
    
    def get(self, request):
        videos1 = Videos.objects.all()
        serializer = videosSerializer(videos1, many = True)
        return Response(serializer.data)

    def post(self):
        pass