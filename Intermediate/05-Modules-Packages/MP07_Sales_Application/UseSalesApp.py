"""
Archivo principal para demostrar el uso de la aplicación de ventas.
"""

from Sales_Application.sales_manager import GestorVentas

def main():
    precio_base = 100.0
    impuesto_porcentaje = 0.05
    descuento_porcentaje = 0.10
    
    gestor = GestorVentas(precio_base, impuesto_porcentaje, descuento_porcentaje)
    precio_final = gestor.calcular_precio_final()
    
    print(f"Precio Base: S/.{precio_base}")
    print(f"Impuesto: {impuesto_porcentaje * 100}%")
    print(f"Descuento: {descuento_porcentaje * 100}%")
    print(f"Precio final: S/.{precio_final}")
    
if __name__ == "__main__":
    main()