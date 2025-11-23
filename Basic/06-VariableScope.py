# ==========================================
#               ÁMBITO LOCAL
# ==========================================

# Variable global: accesible desde cualquier parte del programa
global_var = 20

def mi_funcion():
    """
    Demostración de una variable local.
    Las variables locales solo existen dentro de la función.
    """
    local_var = 10
    print(local_var)  # Se puede imprimir porque está dentro del mismo ámbito

def mi_funcion_dos():
    """
    Accede a una variable global.
    Aquí se utiliza la variable global_var definida fuera de esta función.
    """
    print(global_var)

# Ejemplo de uso:
# mi_funcion_dos()


# ==========================================
#               ÁMBITO GLOBAL
# ==========================================

# Variable global usada como contador
COUNT = 0

def incremento_valor():
    """
    Modifica una variable global usando la palabra clave 'global'.
    Esto permite alterar el valor de COUNT desde dentro de la función.
    """
    global COUNT
    COUNT += 1

# Llamamos a la función para incrementar el contador
incremento_valor()

# Mostramos el valor actualizado de COUNT
print(COUNT)