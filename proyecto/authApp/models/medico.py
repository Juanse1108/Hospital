from django.db import models
from .persona import Persona

class Medico(models.Model):
    anio_contrato=models.IntegerField()
    especialidad=models.CharField(max_length=30,null=False)
    area=models.CharField(max_length=30)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    