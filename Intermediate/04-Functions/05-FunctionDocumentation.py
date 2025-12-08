# -----------------------------------------------------------
# Ejemplo general de documentación de una función
# -----------------------------------------------------------

def mi_funcion(param1, param2):
    """
   Breve descripción de lo que hace la función.

    Parámetros:
        param1 (tipo): Descripción del primer parámetro.
        param2 (tipo): Descripción del segundo parámetro.

    Retorna:
        tipo: Descripción del valor retornado.

    Ejemplo:
        >>> mi_funcion(1, 2)
        3
    """
    return param1 + param2

# -----------------------------------------------------------
# Ejemplo adicional: función sumar
# -----------------------------------------------------------

def sumar(a, b):
    """
    Suma dos números y retorna el resultado.

    Parámetros:
        a (int, float): Primer número a sumar.
        b (int, float): Segundo número a sumar.

    Retorna:
        int, float: La suma de los dos números.

    Ejemplos:
        >>> sumar(3, 5)
        8
        >>> sumar(2.5, 4.5)
        7.0
    """
    return a + b

# -----------------------------------------------------------
# Notas sobre Sphinx para documentación automática
# -----------------------------------------------------------
"""
Sphinx: Herramienta para generar documentación en HTML, PDF y otros formatos a partir de docstrings en el código fuente.
Sphinx puede usar docstrings en formatos como Google o NumPy/SciPy.
pip install sphinx
"""