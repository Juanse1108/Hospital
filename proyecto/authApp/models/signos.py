from django.db import models
from .historico import Historico

class SignosVitales(models.Model):
    id_codigo=models.AutoField(primary_key=True)
    oximetria=models.CharField( max_length=45)
    frecuencia_respiratoria=models.CharField( max_length=45)
    frecuencia_cardica=models.CharField( max_length=45)
    temperatura=models.CharField( max_length=45)
    presion_arterial=models.CharField( max_length=45)
    glicemia=models.CharField( max_length=45)
    fecha=models.DateField()
    historico_cedula=models.ForeignKey(Historico,null=False, blank=False, on_delete=models.CASCADE)   