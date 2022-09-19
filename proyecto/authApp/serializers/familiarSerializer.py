from rest_framework import serializers
from authApp.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'
          