"""
==================================================
              Introducción a Tkinter
==================================================
"""

import tkinter as tk

# --------------------------------------------------
# Funciones (Eventos)
# --------------------------------------------------

def mostrar_texto():
    """
    Captura el texto ingresado en el Entry
    y lo muestra en la etiqueta.
    """
    texto = entrada.get()
    etiqueta.config(text = f"Texto ingresado: {texto}")

def mostrar_mensaje():
    """
    Muestra un mensaje fijo cuando se presiona el botón.
    """
    etiqueta.config(text = "¡Botón presionado!")

# --------------------------------------------------
# Creación de la ventana principal
# --------------------------------------------------

ventana = tk.Tk()
ventana.title("Ventana Básica con Tkinter")

# Establecer el tamaño de la ventana

ventana.geometry("300x200")

# --------------------------------------------------
# Creación de Widgets
# --------------------------------------------------

# Etiqueta (Label)
etiqueta = tk.Label(
    ventana,
    text = "Hola mundo desde Tkinter!"
)
etiqueta.pack(pady = 10)

# Campo de entrada de texto (Entry)
entrada = tk.Entry(ventana)
entrada.pack(pady = 5)

# Botón 1: Muestra el texto ingresado
boton_texto = tk.Button(
    ventana,
    text = "Mostrar texto",
    command = mostrar_texto
)
boton_texto.pack(pady = 5)

# Botón 2: Muestra un mensaje fijo
boton_mensaje = tk.Button(
    ventana,
    text = "Mostrar mensaje",
    command = mostrar_mensaje
)
boton_mensaje.pack(pady = 5)

# --------------------------------------------------
# Bucle principal de la aplicación
# --------------------------------------------------
# Mantiene la ventana abierta y escuchando eventos

ventana.mainloop()