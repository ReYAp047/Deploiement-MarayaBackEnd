from rest_framework import serializers
from .models import APropos 

class actionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = APropos
        fields = '__all__'