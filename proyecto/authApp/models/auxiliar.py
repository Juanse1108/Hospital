from django.db import models
from .persona import Persona
from .rol import Rol

class Auxiliar(models.Model):
    cargo=models.CharField(max_length=45)
    fecha_contrato=models.DateField()
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)