"""
Módulo donde se calcula el precio final del producto considerando
precio base, impuestos y descuentos.
"""

class Precios:
    @staticmethod
    def calcular_precio_final(precio_base, impuesto, descuento):
        return precio_base + impuesto - descuento