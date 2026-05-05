from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
import re

class PagoForm(forms.Form):
    titular = forms.CharField(max_length=100)
    numero_tarjeta = forms.CharField(max_length=19)
    fecha_expiracion = forms.CharField(max_length=5)
    cvv = forms.CharField(max_length=3, min_length=3)
    monto = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

    # Validación Nivel 2: Solo números en la tarjeta
    def clean_numero_tarjeta(self):
        data = self.cleaned_data.get('numero_tarjeta')
        num_limpio = data.replace(' ', '')
        if not num_limpio.isdigit():
            raise ValidationError("El número de tarjeta debe contener únicamente dígitos.")
        if len(num_limpio) != 16:
            raise ValidationError("El número de tarjeta debe tener 16 dígitos.")

        return num_limpio

    # Validación Nivel 2: Formato y validez de la fecha
    def clean_fecha_expiracion(self):
        fecha = self.cleaned_data.get('fecha_expiracion')
        
        # Expresión regular para asegurar formato MM/AA
        if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', fecha):
            raise ValidationError("El formato de expiración debe ser MM/AA.")
        
        mes, anio = fecha.split('/')
        
        # Validar que la tarjeta no esté vencida
        try:
            # Asumimos que "AA" es del 2000 en adelante
            fecha_exp = datetime(int(f"20{anio}"), int(mes), 1)
            # Para la validación estricta, comparamos con el mes/año actual
            hoy = datetime.now()
            if fecha_exp.year < hoy.year or (fecha_exp.year == hoy.year and fecha_exp.month < hoy.month):
                raise ValidationError("Esta tarjeta ya ha expirado.")
        except ValueError:
            raise ValidationError("Fecha inválida.")
            
        return fecha

    # Validación Nivel 2: CVV numérico
    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        if not cvv.isdigit():
            raise ValidationError("El código de seguridad (CVV) debe ser numérico.")
        return cvv