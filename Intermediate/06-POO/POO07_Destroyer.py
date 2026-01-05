"""
==================================================
            DESTRUCTOR EN POO (__del__)
==================================================

El método __del__ se conoce como destructor.
Se ejecuta cuando un objeto es eliminado de
la memoria por el recolector de basura.

⚠ Importante:
No se debe depender exclusivamente de __del__
para liberar recursos críticos, ya que su
ejecución no es determinística.
"""

# ==================================================
#                   CLASE ARCHIVO
# ==================================================

class Archivo:
    """
    Clase que maneja la apertura y cierre
    de un archivo utilizando un destructor.
    """
    
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, "w", encoding="utf-8")
        print(f"Archivo '{self.nombre_archivo}' abierto")
        
    def escribir(self, contenido):
        """
        Escribe contenido en el archivo.
        """
        self.archivo.write(contenido)
        
    def __del__(self):
        """
        Destructor que se encarga de cerrar
        el archivo cuando el objeto es eliminado.
        """
        self.archivo.close() # Cierre del archivo
        print(f"Archivo '{self.nombre_archivo}' cerrado")

# ==================================================
#                 EJEMPLO DE USO
# ==================================================

archivo = Archivo("Intermediate/06-POO/ejemplo.txt")
archivo.escribir("Hola desde el curso de Python!")

# Eliminamos explícitamente el objeto
del archivo  # Fuerza la llamada al destructor