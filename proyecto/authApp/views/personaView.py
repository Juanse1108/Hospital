from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.personaSerializer import PersonaSerializer
from authApp.models.persona import Persona

class PersonaView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = PersonaSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        persona = Persona.objects.all()
        serializer = PersonaSerializer(persona,many=True)
        return Response(serializer.data)