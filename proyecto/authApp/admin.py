from django.contrib import admin
from .models.rol import Rol
from .models.persona import Persona
from .models.auxiliar import Auxiliar
from .models.familiar import Familiar
from .models.medico import Medico
from .models.enfermera import Enfermera
from .models.paciente import Paciente
from .models.sugerencias import Sugerencias
from .models.historico import Historico
from .models.signos import SignosVitales
# Register your models here.
admin.site.register(Rol)
admin.site.register(Persona)
admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(Medico)
admin.site.register(Enfermera)
admin.site.register(Paciente)
admin.site.register(Sugerencias)
admin.site.register(Historico)
admin.site.register(SignosVitales)