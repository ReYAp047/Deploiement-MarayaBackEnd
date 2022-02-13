from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Historique.models import Historique
from .serializers import historiqueSerializer

class HistoriqueList(APIView):
    serializer_class  = historiqueSerializer

    def get_queryset(self):
        Historiques = Historique.objects.all()
        return Historiques
    
    def get(self, request):
        Historique1 = Historique.objects.all()
        serializer = historiqueSerializer(Historique1, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        historique_data = request.data

        new_histo = Historique.objects.create(Nom_Prenom=historique_data["Nom_Prenom"], Email=historique_data[
            "Email"], NomAction=historique_data["NomAction"], Montant=historique_data["Montant"], Date=historique_data["Date"])

        new_histo.save()

        serializer = historiqueSerializer(new_histo)

        return Response(serializer.data)