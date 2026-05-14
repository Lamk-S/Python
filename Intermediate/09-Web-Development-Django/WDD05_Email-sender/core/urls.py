from django.urls import path
from .views import listar_empleados

urlpatterns = [
    path('', listar_empleados, name="listar_empleados"),
]