from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PagoForm
from .models import TransaccionPago

def procesar_pago_view(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        
        if form.is_valid():
            # Extraemos los datos limpios y validados
            titular = form.cleaned_data['titular']
            monto = form.cleaned_data['monto']
            numero_tarjeta = form.cleaned_data['numero_tarjeta']
            
            # REGLA DE ORO: Solo se guaradará los últimos 4 dígitos
            ultimos_digitos = numero_tarjeta[-4:]
            
            # Guardar la transacción en la base de datos
            TransaccionPago.objects.create(
                titular=titular,
                monto=monto,
                ultimos_digitos=ultimos_digitos,
                estado='APROBADO'  # En la vida real, se esperaría respuesta(ejem. PayPal)
            )
            
            # Mensaje de éxito global
            messages.success(request, f'¡Pago de ${monto} procesado exitosamente para {titular}!')
            return redirect('procesar_pago') # Redirige a la misma URL para limpiar la petición POST
            
        else:
            # Mensaje de error global
            messages.error(request, 'La transacción no pudo completarse. Revisa los errores en el formulario.')
            
    else:
        # Si es una petición GET, mostramos el formulario vacío
        form = PagoForm()
        
    return render(request, 'forms_core/pago.html', {'form': form})