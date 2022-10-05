from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.sugerenciasSerializer import SugerenciasSerializer
from authApp.models.sugerencias import Sugerencias

class SugerenciasView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = SugerenciasSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        sugerencia = Sugerencias.objects.all()
        serializer = SugerenciasSerializer(sugerencia,many=True)
        return Response(serializer.data)