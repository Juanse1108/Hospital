from rest_framework import serializers
from authApp.models.historico import Historico

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'