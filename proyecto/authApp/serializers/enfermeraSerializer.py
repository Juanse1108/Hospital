from rest_framework import serializers
from authApp.models.enfermera import Enfermera

class EnfermeraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermera
        fields = '__all__'