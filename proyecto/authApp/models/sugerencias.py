from django.db import models
from .medico import Medico
from .historico import Historico

class Sugerencias(models.Model):
    id_codigo=models.PositiveIntegerField(primary_key=True)
    diagnostico=models.CharField( max_length=45)
    recomendaciones=models.CharField( max_length=45)
    fecha=models.DateField()
    historico_cedula=models.ForeignKey(Historico,null=False, blank=False, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Medico,null=False, blank=False, on_delete=models.CASCADE)