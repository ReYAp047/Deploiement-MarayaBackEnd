from rest_framework import serializers
from .models import Q_On_Fait 

class actionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_On_Fait
        fields = '__all__'