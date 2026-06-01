from django.urls import path
from .views import listar_empleados, enviar_correo

urlpatterns = [
    path('', listar_empleados, name="listar_empleados"),
    path('enviar-correo/', enviar_correo, name="enviar_correo"),
]