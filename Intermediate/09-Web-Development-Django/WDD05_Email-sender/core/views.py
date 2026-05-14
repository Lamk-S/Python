from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Empleados
from .forms import EnviarCorreoForm
from django.core.mail import send_mail

def listar_empleados(request):
    empleados = Empleados.objects.all()
    context = {
        "empleados": empleados
    }
    
    return render(request, 'empleados/listar_empleados.html', context)