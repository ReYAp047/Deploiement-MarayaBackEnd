from rest_framework import serializers
from .models import Facebook 

class actionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = '__all__'