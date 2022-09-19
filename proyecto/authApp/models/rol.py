from django.db import models

class Rol(models.Model):
    codigo_rol=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=45)
    activo=models.CharField(max_length=10)