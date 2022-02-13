from rest_framework import serializers
from .models import Historique

class historiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historique
        fields = '__all__'