from django.db import models
from .persona import Persona

class Enfermera(models.Model):
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    area=models.CharField(max_length=30)
    anio_contrato=models.IntegerField()