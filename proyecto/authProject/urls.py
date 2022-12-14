"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rol/', views.RolView.as_view()),
    path('persona/', views.PersonaView.as_view()),
    path('medico/', views.MedicoView.as_view()),
    path('paciente/', views.PacienteView.as_view()),
    path('paciente/<int:pk>/', views.PacienteDetalladoView.as_view()),
    path('familiar/', views.FamiliarView.as_view()),
    path('enfermera/', views.EnfermeraView.as_view()),
    path('auxiliar/', views.AuxiliarView.as_view()),
    path('historico/', views.HistoricoView.as_view()),
    path('signosVitales/', views.SignosView.as_view),
    path('sugerencias/', views.SugerenciasView.as_view),
]
