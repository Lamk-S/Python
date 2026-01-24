"""
==================================================
        Conversor de Moneda con PyQt6
==================================================

Este ejemplo demuestra:
- Uso de PyQt6 con Qt Designer
- Separación de diseño (.ui / archivo generado)
  y lógica de la aplicación
- Manejo de eventos (signals & slots)
- Validación básica de datos de entrada
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from dollar_design import Ui_MainWindow

# ==================================================
# Clase principal de la aplicación
# ==================================================

class MiApp(QMainWindow):
    """
    Clase principal que hereda de QMainWindow.
    Aquí se conecta la interfaz gráfica con la lógica.
    """
    
    def __init__(self):
        super(MiApp, self).__init__()
        
        # ----------------------------------------------
        # Inicialización de la interfaz
        # ----------------------------------------------
        # Se carga la UI creada en Qt Designer
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ----------------------------------------------
        # Conexión de eventos
        # ----------------------------------------------
        # Al presionar el botón, se ejecuta el método conversion
        
        self.ui.btnCambiar.clicked.connect(self.conversion)
    
    # ==================================================
    # Lógica de negocio
    # ==================================================
        
    def conversion(self):
        """
        Convierte un monto en soles a dólares usando
        el tipo de cambio ingresado por el usuario.
        """
        
        try:
            # Obtener valores desde los campos de texto
            soles = float(self.ui.txtMontoSoles.toPlainText())
            cambio = float(self.ui.txtTipoCambio.toPlainText())

            # Validación simple
            if cambio <= 0:
                self.ui.txtMontoObtenido.setText("Tipo de cambio inválido")
                return

            # Conversión de moneda
            dolares = soles / cambio

            # Mostrar resultado
            self.ui.txtMontoObtenido.setText(f"Dólares: ${dolares:.2f}")

        except ValueError:
            # Manejo de errores si el usuario ingresa texto no numérico
            self.ui.txtMontoObtenido.setText("Ingrese valores numéricos")

# ==================================================
# Punto de entrada de la aplicación
# ==================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiApp()
    window.show()
    sys.exit(app.exec())