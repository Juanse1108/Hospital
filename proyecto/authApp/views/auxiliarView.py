from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.auxiliarSerializer import AuxiliarSerializer
from authApp.models.auxiliar import Auxiliar

class AuxiliarView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = AuxiliarSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        auxiliar = Auxiliar.objects.all()
        serializer = AuxiliarSerializer(auxiliar,many=True)
        return Response(serializer.data)