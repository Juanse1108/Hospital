from django.db import models
from .paciente import Paciente

class Historico(models.Model):
    paciente=models.OneToOneField(Paciente,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    codigo=models.PositiveIntegerField()
    en_cuidado=models.CharField(max_length=2)