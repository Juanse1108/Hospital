from rest_framework import status,views
from rest_framework.response import Response
from authApp.serializers.signosSerializer import SignosSerializer
from authApp.models.signos import SignosVitales

class SignosView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = SignosSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        signo = SignosVitales.objects.all()
        serializer = SignosSerializer(signo,many=True)
        return Response(serializer.data)