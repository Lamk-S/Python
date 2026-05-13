from django.core.exceptions import ValidationError

def validar_algoritmo_luhn(numero_tarjeta):
    """
    Valida un número de tarjeta de crédito utilizando el Algoritmo de Luhn (Módulo 10).
    """
    # 1. Quitar espacios por seguridad (aunque ya vengan limpios del form)
    numero_limpio = numero_tarjeta.replace(" ", "")
    
    if not numero_limpio.isdigit():
        raise ValidationError("El número de tarjeta debe contener únicamente dígitos.")
        
    # 2. Aplicar la lógica de Luhn
    suma = 0
    # Invertir el string del número para procesarlo de derecha a izquierda
    digitos_invertidos = numero_limpio[::-1]
    
    for i, digito_str in enumerate(digitos_invertidos):
        digito = int(digito_str)
        
        # Duplicar el valor de los dígitos en posiciones impares (1, 3, 5...) 
        # Nota: en Python el índice empieza en 0, así que usamos i % 2 != 0
        if i % 2 != 0:
            digito *= 2
            # Si al duplicar el número es mayor a 9, restamos 9 (ej. 7*2=14 -> 14-9=5)
            if digito > 9:
                digito -= 9
                
        suma += digito

    # 3. Si el módulo de 10 es 0, la tarjeta es matemáticamente válida
    if suma % 10 != 0:
        raise ValidationError("El número de tarjeta es inválido (Falló la validación de Luhn).")