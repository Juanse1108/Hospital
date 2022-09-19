from rest_framework import serializers
from authApp.models.sugerencias import Sugerencias

class SugerenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugerencias
        fields = '__all__'