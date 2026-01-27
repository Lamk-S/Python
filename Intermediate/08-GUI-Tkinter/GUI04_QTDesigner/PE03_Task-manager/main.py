"""
==================================================
        Gestor de Tareas con PyQt6
==================================================

Este ejemplo demuestra:
- Uso de PyQt6 con Qt Designer
- Separación de interfaz y lógica
- Manejo de listas mediante QStringListModel
- Estados de tareas (pendiente / completada)
- Validación de entradas del usuario
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QStringListModel

# Interfaz creada en Qt Designer
from task_manager import Ui_MainWindow

# ==================================================
# Clase principal de la aplicación
# ==================================================

class MiApp(QMainWindow):
    """
    Clase principal del gestor de tareas.
    """
    
    def __init__(self):
        super().__init__()

        # ----------------------------------------------
        # Inicialización de la interfaz
        # ----------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ----------------------------------------------
        # Modelo para la lista de tareas
        # ----------------------------------------------
        self.modelo_tareas = QStringListModel()
        self.ui.listTasks.setModel(self.modelo_tareas)
        
        # Lista interna de tareas
        # Cada tarea es un diccionario:
        # { "texto": str, "completada": bool }
        self.tareas = []
        
        # ----------------------------------------------
        # Conexión de eventos
        # ----------------------------------------------
        self.ui.btnAdd.clicked.connect(self.agregar_tarea)
        self.ui.btnComplete.clicked.connect(self.marcar_completada)
        self.ui.btnDelete.clicked.connect(self.eliminar_tarea)
        
        # Inicializar contador
        self.actualizar_contador()
    
    # ==================================================
    # Lógica
    # ==================================================
    
    def agregar_tarea(self):
        """
        Agrega una nueva tarea como pendiente.
        """
        
        texto = self.ui.txtTask.toPlainText().strip()
        
        if not texto:
            QMessageBox.warning(
                self,
                "Entrada inválida",
                "La tarea no puede estar vacía."
            )
            return
        
        self.tareas.append({
            "texto": texto,
            "completada": False
        })
        
        self.ui.txtTask.clear()
        self.actualizar_lista()
        self.actualizar_contador()
        
    def marcar_completada(self):
        """
        Marca la tarea seleccionada como completada.
        """
        
        index = self.ui.listTasks.currentIndex()
        
        if not index.isValid():
            QMessageBox.information(
                self,
                "Selección requerida",
                "Seleccione una tarea."
            )
            return
        
        self.tareas[index.row()]["completada"] = True
        self.actualizar_lista()
        self.actualizar_contador()
        
    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada.
        """
        
        index = self.ui.listTasks.currentIndex()

        if not index.isValid():
            QMessageBox.information(
                self,
                "Selección requerida",
                "Seleccione una tarea."
            )
            return
        
        self.tareas.pop(index.row())
        self.actualizar_lista()
        self.actualizar_contador()
    
    # ==================================================
    # Métodos auxiliares
    # ==================================================
    
    def actualizar_lista(self):
        """
        Actualiza el modelo visual de la lista.
        """
        
        tareas_formateadas = []

        for tarea in self.tareas:
            estado = "✔" if tarea["completada"] else "⏳"
            tareas_formateadas.append(f"{estado} {tarea['texto']}")

        self.modelo_tareas.setStringList(tareas_formateadas)
        
    def actualizar_contador(self):
        """
        Actualiza el contador de tareas pendientes.
        """
        
        pendientes = sum(
            1 for tarea in self.tareas if not tarea["completada"]
        )

        self.ui.lblPending.setText(
            f"Tareas pendientes: {pendientes}"
        )
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiApp()
    window.show()
    sys.exit(app.exec())