from rest_framework import serializers
from authApp.models.signos import SignosVitales

class SignosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'