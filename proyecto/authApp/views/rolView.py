from rest_framework import status,views
from rest_framework.response import Response
from authApp.models.rol import Rol
from authApp.serializers.rolSerializer import RolSerializer

class RolView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializers = RolSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            stringResponse={'detail':'Se guardo correctamente'}
            return Response(stringResponse,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        rol = Rol.objects.all()
        serializer = RolSerializer(rol,many=True)
        return Response(serializer.data)