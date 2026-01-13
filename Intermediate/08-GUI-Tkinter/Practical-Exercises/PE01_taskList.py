"""
==================================================
           Lista de tareas con Tkinter
==================================================

Este ejercicio integra:
- Ventanas y Frames
- Widgets (Listbox, Entry, Button, Scrollbar)
- Manejo de eventos
- Separación de lógica y presentación
"""

import tkinter as tk
from tkinter import messagebox

# ==================================================
# Funciones de lógica (acciones)
# ==================================================

def agregar_tarea(entrada, lista):
    tarea = entrada.get()
    if tarea:
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
        
def eliminar_tarea(lista):
    tarea_seleccionada = lista.curselection()
    if  tarea_seleccionada:
        lista.delete(tarea_seleccionada)

def salir(ventana):
    if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
        ventana.destroy()
        
# ==================================================
# Función principal de la aplicación
# ==================================================

def principal():
    
    # ----------------------------------------------
    # Ventana principal
    # ----------------------------------------------
    # Contenedor principal de la aplicación
    
    ventana = tk.Tk()
    ventana.title("Lista tareas")
    
    # ----------------------------------------------
    # Frame de la lista de tareas
    # ----------------------------------------------
    # Agrupa el Listbox y el Scrollbar
    
    marco_lista = tk.Frame(ventana)
    marco_lista.pack(pady=10)
    
    lista_tareas = tk.Listbox(marco_lista, width=50, height=10)
    lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)
    
    scrollbar = tk.Scrollbar(marco_lista, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Conectar scrollbar con listbox
    lista_tareas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista_tareas.yview)
    
    # ----------------------------------------------
    # Frame de entrada de datos
    # ----------------------------------------------
    # Permite ingresar nuevas tareas
    
    marco_entrada = tk.Frame(ventana)
    marco_entrada.pack(pady=5)
    
    etiqueta_tarea = tk.Label(marco_entrada, text="Nueva Tarea:")
    etiqueta_tarea.pack(side=tk.LEFT)
    entrada_tarea = tk.Entry(marco_entrada, width=40)
    entrada_tarea.pack(side=tk.LEFT)
    
    # ----------------------------------------------
    # Botones de acción
    # ----------------------------------------------
    
    btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=lambda:agregar_tarea(entrada_tarea, lista_tareas))
    btn_agregar.pack(pady=5)
    
    btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=lambda:eliminar_tarea(lista_tareas))
    btn_eliminar.pack(pady=5)
    
    btn_salir = tk.Button(ventana, text="Salir", command=lambda:salir(ventana))
    btn_salir.pack(pady=5)
    
    # ----------------------------------------------
    # Bucle principal
    # ----------------------------------------------
    # Mantiene la aplicación activa
    
    ventana.mainloop()
    
# ==================================================
# Punto de entrada del programa
# ==================================================

if __name__ == "__main__":
    principal()