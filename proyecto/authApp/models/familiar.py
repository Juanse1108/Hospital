from django.db import models
from .persona import Persona

class Familiar(models.Model):
    parentesco=models.CharField(max_length=45,null=False)
    identificacion=models.OneToOneField(Persona,null=False, blank=False, on_delete=models.CASCADE,primary_key=True)