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

def enviar_correo(request):
    if request.method == 'POST':
        form = EnviarCorreoForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            correo_destino = request.POST.get('correo')
            send_mail(asunto, mensaje, 'kunlancelot@gmail.com', [correo_destino])
            return JsonResponse({'status': 'success', 'message': 'Correo enviado exitosamente'})
    return JsonResponse({'status': 'error', 'message': 'Error al enviar el correo'})