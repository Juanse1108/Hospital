from django.db import models
from .rol import Rol

class Persona(models.Model):
    identificacion=models.CharField(max_length=10,primary_key=True)
    tipo_documento=models.CharField(max_length=2)
    nombre=models.CharField(max_length=45 )
    apellido=models.CharField(max_length=45)
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=2)
    email=models.EmailField(max_length=45, unique=True)    
    telefono=models.CharField(max_length=10)
    direccion=models.CharField(max_length=45)
    ciudad=models.CharField(max_length=45)
    fecha_registro=models.DateField()
    codigo_rol=models.ForeignKey(Rol,null=False, blank=False, on_delete=models.CASCADE)
    password= models.CharField( max_length=45)