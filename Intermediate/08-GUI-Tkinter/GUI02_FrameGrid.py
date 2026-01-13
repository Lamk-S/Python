"""
==================================================
          Uso de Frame y Grid en Tkinter
==================================================
"""

import tkinter as tk

# --------------------------------------------------
# Creación de la ventana principal
# --------------------------------------------------

ventana = tk.Tk()
ventana.title("Uso de Frame y Grid")

# --------------------------------------------------
# Creación del Frame (contenedor)
# --------------------------------------------------
# Frame permite agrupar widgets dentro de la ventana

frame = tk.Frame(
    ventana,
    borderwidth = 2,
    relief = "groove"
)
frame.pack(
    padx = 10,
    pady = 10,
    fill = "both",
    expand = True
)

# --------------------------------------------------
# Creación de Widgets dentro del Frame
# --------------------------------------------------
# Usamos grid() para organizar los widgets en filas y columnas

etiqueta1 = tk.Label(frame, text = "Etiqueta 1")
etiqueta1.grid(row = 0, column = 0, padx = 10, pady = 5)

etiqueta2 = tk.Label(frame, text = "Etiqueta 2")
etiqueta2.grid(row = 0, column = 1, padx = 10, pady = 5)

boton1 = tk.Button(frame, text = "Botón 1")
boton1.grid(row = 1, column = 0, padx = 10, pady = 5)

boton2 = tk.Button(frame, text = "Botón 2")
boton2.grid(row = 1, column = 1, padx = 10, pady = 5)

# --------------------------------------------------
# Bucle principal de la aplicación
# --------------------------------------------------
# Mantiene la ventana activa y escuchando eventos

ventana.mainloop()