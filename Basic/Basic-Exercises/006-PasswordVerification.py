"""
Descripción:
Ejemplos básicos del uso de la función any() en Python, seguido de una función
que verifica si una contraseña cumple con criterios mínimos de seguridad.
"""

# ===================================
#        EJEMPLOS DE any()
# ===================================

def ejemplo_any_001():
    """
    Ejemplo 001:
    La función any() devuelve True si al menos un elemento de la secuencia
    es True. En este caso, la lista contiene un valor True.
    """
    valores = [False, False, True]
    resultado = any(valores)
    print("Resultado ejemplo 001:", resultado)


def ejemplo_any_002():
    """
    Ejemplo 002:
    En listas numéricas, any() devuelve True si existe un número distinto de 0,
    ya que 0 equivale a False y cualquier otro número equivale a True.
    """
    numeros = [0, 0, 0, 5]
    resultado = any(numeros)
    print("Resultado ejemplo 002:", resultado)


def ejemplo_any_003():
    """
    Ejemplo 003:
    Una lista vacía siempre devuelve False con any(), ya que no contiene
    ningún valor True.
    """
    vacia = []
    resultado = any(vacia)
    print("Resultado ejemplo 003:", resultado)


# ===================================
#      VERIFICACIÓN DE CONTRASEÑA
# ===================================

def verificar_contrasena(contrasena):
    # Verificar longitud mínima
    if len(contrasena) < 8:
        return False

    # Verificar presencia de al menos un dígito
    if not any(char.isdigit() for char in contrasena):
        return False

    # Verificar presencia de al menos una letra mayúscula
    if not any(char.isupper() for char in contrasena):
        return False

    # Verificar presencia de al menos un carácter especial
    caracteres_especiales = "@#$%^&*()-_+=!"
    if not any(char in caracteres_especiales for char in contrasena):
        return False

    # Si cumple todas las condiciones, es segura
    return True


# ===================================
#           EJEMPLO DE USO
# ===================================

# Ejecución de ejemplos de any()
ejemplo_any_001()
ejemplo_any_002()
ejemplo_any_003()

# Ejemplo de verificación de contraseña
clave = "Segur@123"
print("¿Contraseña segura?:", verificar_contrasena(clave))
