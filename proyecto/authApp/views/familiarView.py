from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.familiarSerializer import FamiliarSerializer
from authApp.models.familiar import Familiar

class FamiliarView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = FamiliarSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        familiar = Familiar.objects.all()
        serializer = FamiliarSerializer(familiar,many=True)
        return Response(serializer.data)