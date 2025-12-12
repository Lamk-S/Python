import unittest
from Sales_Application.sales_manager import GestorVentas
from Sales_Application.exceptions import ImpuestoInvalidoError, DescuentoInvalidoError

class TestGestorVentas(unittest.TestCase):
    def test_calculo_precio_final(self):
        gestor = GestorVentas(100.0, 0.05, 0.10)
        self.assertEqual(gestor.calcular_precio_final(), 95.0)
        
    def test_impuesto_invalido(self):
        with self.assertRaises(ImpuestoInvalidoError):
            GestorVentas(100.0, 1.5, 0.10)
    
    def test_descuento_invalido(self):
        with self.assertRaises(DescuentoInvalidoError):
            GestorVentas(100.0, 0.05, 1.5)

if __name__ == "__main__":
    unittest.main()
    
# Ejecutar los tests:
# python -m unittest discover -s test
