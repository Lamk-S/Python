"""
Módulo principal que coordina los cálculos de precios en la aplicación de ventas.
"""

from .discounts import Descuentos
from .taxes import Impuestos
from .prices import Precios

class GestorVentas:
    """
    Clase encargada de gestionar el cálculo del precio final de un producto.
    """
    def __init__(self, precio_base, impuesto_porcentaje, descuento_porcentaje):
        self.precio_base = precio_base
        self.impuesto = Impuestos(impuesto_porcentaje)
        self.descuento = Descuentos(descuento_porcentaje)
        
    def calcular_precio_final(self):
        """
        Calcula el precio final del producto aplicando impuesto y descuento.
        """
        impuesto_aplicado = self.impuesto.aplicar_impuesto(self.precio_base)
        descuento_aplicado = self.descuento.aplicar_descuento(self.precio_base)
        precio_final = Precios.calcular_precio_final(self.precio_base, impuesto_aplicado, descuento_aplicado)
        return round(precio_final, 2)