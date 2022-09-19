from django.db import models
from .medico import Medico
from .persona import Persona
from .familiar import Familiar
from .enfermera import Enfermera


class Paciente(models.Model):
    cedula_familiar=models.ForeignKey(Familiar,null=False, blank=False, on_delete=models.CASCADE)
    georreferencia= models.CharField( max_length=45)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)
    cedula_doctor=models.ForeignKey(Medico, on_delete=models.CASCADE)
    cedula_enfermera=models.ForeignKey(Enfermera,null=False, blank=False, on_delete=models.CASCADE)