"""
==================================================
        EJERCICIO PRÁCTICO: GESTOR DE TAREAS
==================================================

Este ejercicio refuerza:
- Diseño de clases
- Encapsulación de estado
- Manejo de listas de objetos
- Interacción por consola
"""

# ==================================================
#                   CLASE TASK
# ==================================================

class Task:
    """
    Representa una tarea individual.
    """
    
    def __init__(self, title, description = ""):
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_as_completed(self):
        self.completed = True
    
    def __str__(self):
        status = "✔️ " if self.completed else "❌"
        return f"{status} {self.title} - {self.description}"

# ==================================================
#               CLASE TASK MANAGER
# ==================================================

class TaskManager:
    """
    Administra un conjunto de tareas.
    """
    
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description = ""):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Tarea '{title}' agregada correctamente.")
    
    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas en la lista")
            return
        
        print("\nLista de tareas")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    
    def mark_task_completed(self, index):
        try:
            task = self.tasks[index - 1]
            if task.completed:
                print(f"La tarea '{task.title}' ya está completada.")
            else:
                task.mark_as_completed()
                print(f"Tarea '{task.title}' marcada como completada.")
        except IndexError:
            print("Índice de tarea no válido. Intente nuevamente.")
    
    def delete_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            print(f"Tarea '{task.title}' eliminada correctamente.")
        except IndexError:
            print("Índice de tarea no válido. Intente nuevamente.")
    
    # ==================================================
    #               CICLO PRINCIPAL
    # ==================================================
    
    def start(self):
        while True:
            print("\nGestor de tareas")
            print("1. Agregar la tarea")
            print("2. Listar tareas")
            print("3. Marcar tarea como completada")
            print("4. Eliminar la tarea")
            print("5. Salir")
            
            choice = input("Seleccione una opción: ").strip()
            
            if choice == "1":
                title = input("Título de la tarea: ").strip()
                description = input("Descripción (opcional): ").strip()
                self.add_task(title, description)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                try:
                    index = int(input("Índice de la tarea: ").strip())
                    self.mark_task_completed(index)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            elif choice == "4":
                try:
                    index = int(input("Índice de la tarea: ").strip())
                    self.delete_task(index)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            elif choice == "5":
                print("Saliendo del gestor de tareas...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                
# ==================================================
#                 EJECUCIÓN PRINCIPAL
# ==================================================

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start()