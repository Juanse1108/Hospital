from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.pacienteSerializer import PacienteSerializer
from authApp.models.paciente import Paciente
from django.http import Http404

class PacienteView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = PacienteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        paciente = Paciente.objects.all()
        serializer = PacienteSerializer(paciente,many=True)
        return Response(serializer.data)

class PacienteDetalladoView(views.APIView):
    def get_object(self, pk):
        try:
            return Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404    
   
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PacienteSerializer(post)  
        return Response(serializer.data)