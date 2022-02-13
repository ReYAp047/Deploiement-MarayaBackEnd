from rest_framework import serializers
from .models import Actions 
from .models import Images 
from .models import FontImages 
from .models import Partonaire 
from .models import Videos 

class actionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

class imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class fontImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FontImages
        fields = '__all__'



class partonairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partonaire
        fields = '__all__'


class videosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'