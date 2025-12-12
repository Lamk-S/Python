"""
Archivo principal para demostrar el uso de la aplicación de ventas.
"""

from Sales_Application.sales_manager import GestorVentas

# ---------------------------------------------------------------
# Función para solicitar y validar entrada numérica del usuario
# ---------------------------------------------------------------
def pedir_numero(mensaje: str) -> float:
    """Pide un número al usuario y lo valida. Repite hasta obtener uno válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

# ---------------------------------------------------------------
# Función principal del programa
# ---------------------------------------------------------------
def main():
    precio_base = pedir_numero("Ingrese el precio Base: S/.")
    impuesto_porcentaje = pedir_numero("Ingrese el porcentaje de Impuesto (%): ") / 100
    descuento_porcentaje = pedir_numero("Ingrese el porcentaje de Descuento (%): ") / 100
    
    gestor = GestorVentas(precio_base, impuesto_porcentaje, descuento_porcentaje)
    precio_final = gestor.calcular_precio_final()
    
    print(f"Precio Base: S/.{precio_base}")
    print(f"Impuesto: {impuesto_porcentaje * 100}%")
    print(f"Descuento: {descuento_porcentaje * 100}%")
    print(f"Precio final: S/.{precio_final}")
    
if __name__ == "__main__":
    main()