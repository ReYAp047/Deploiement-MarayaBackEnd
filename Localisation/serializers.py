from rest_framework import serializers
from .models import Localisation

class actionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'