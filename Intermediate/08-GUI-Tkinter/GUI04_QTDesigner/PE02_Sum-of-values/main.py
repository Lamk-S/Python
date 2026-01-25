"""
==================================================
        Suma de Valores con PyQt6
==================================================

Este ejemplo demuestra:
- Uso de PyQt6 junto con una interfaz creada en Qt Designer
- Implementación del patrón diseño + lógica
- Uso de QStringListModel para mostrar datos en una lista
- Manejo de eventos (signals & slots)
- Validación de datos de entrada
- Manejo básico de errores con QMessageBox
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QStringListModel

# Interfaz generada desde Qt Designer
from carrito import Ui_MainWindow

# ==================================================
# Clase principal de la aplicación
# ==================================================

class MiApp(QMainWindow):
    """
    Clase principal que conecta la interfaz gráfica
    con la lógica de la aplicación.
    """
    
    def __init__(self):
        super().__init__()

        # ----------------------------------------------
        # Inicialización de la interfaz gráfica
        # ----------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ----------------------------------------------
        # Modelo para el QListView
        # ----------------------------------------------
        # Se usa QStringListModel para manejar la lista
        # de precios mostrados en la interfaz
        self.modelo_precio = QStringListModel()
        self.ui.listPrecios.setModel(self.modelo_precio)
        
        # Lista interna donde se almacenan los precios
        self.lista_precio = []
        
        # ----------------------------------------------
        # Conexión de eventos
        # ----------------------------------------------
        self.ui.btnAgregar.clicked.connect(self.add_price)
    
    # ==================================================
    # Lógica
    # ==================================================
         
    def add_price(self):
        """
        Agrega un precio a la lista y calcula el total.
        """
        
        try:
            # Obtener el texto ingresado por el usuario
            texto_precio = self.ui.txtPrecio.toPlainText().strip()
            
            # Validación básica: campo vacío
            if not texto_precio:
                raise ValueError("Campo vacío")
            
            # Convertir el texto a número
            precio = float(texto_precio)
            
            # Validación adicional
            if precio < 0:
                raise ValueError("Precio negativo")
            
            # Agregar el precio a la lista
            self.lista_precio.append(precio)
            
            # Actualizar el modelo de la lista
            self.modelo_precio.setStringList(
                [f"${p:.2f}" for p in self.lista_precio]
            )
            
            # Calcular el total
            total = sum(self.lista_precio)
            
            # Mostrar el total
            self.ui.txtTotal.setPlainText(f"${total:.2f}")
            
            # Limpiar campos de entrada
            self.ui.txtProducto.clear()
            self.ui.txtPrecio.clear()
        except ValueError:
            QMessageBox.warning(
                self,
                "Error de entrada",
                "Ingrese un precio válido (número positivo)."
            )
        
# ==================================================
# Punto de entrada de la aplicación
# ==================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiApp()
    window.show()
    sys.exit(app.exec())