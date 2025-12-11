"""
Guía básica para crear y usar entornos virtuales en Python.

-------------------------------------------------------------------------------
¿QUÉ ES UN ENTORNO VIRTUAL?
-------------------------------------------------------------------------------
Un entorno virtual es un espacio aislado que permite tener una instalación 
independiente de Python y de sus paquetes. Esto evita conflictos entre 
dependencias de distintos proyectos y permite trabajar con versiones específicas 
sin afectar al sistema ni a otros desarrollos.

-------------------------------------------------------------------------------
INSTALACIÓN PREVIA
-------------------------------------------------------------------------------
Antes de crear un entorno virtual, asegúrate de tener instalado "virtualenv":

    pip install virtualenv

Aunque, en la mayoría de versiones modernas de Python, ya no es necesario ya que
Python incluye el módulo "venv" por defecto.

-------------------------------------------------------------------------------
CÓMO CREAR UN ENTORNO VIRTUAL EN PYTHON
-------------------------------------------------------------------------------

1. Abrir la terminal o línea de comandos.

2. Navegar al directorio del proyecto donde se desea crear el entorno virtual.

3. Ejecutar el siguiente comando para crear un entorno virtual:
       python -m venv nombre_del_entorno

   (Reemplazar "nombre_del_entorno" con el nombre deseado.)

-------------------------------------------------------------------------------
ACTIVAR Y USAR EL ENTORNO VIRTUAL
-------------------------------------------------------------------------------

► En Windows (PowerShell):

   Si es la primera vez, puede que necesites habilitar la ejecución de scripts:
       Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

   Luego:

   a) Activar el entorno:
          .\nombre_del_entorno\Scripts\Activate

   b) Instalar paquetes dentro del entorno (ejemplo):
          pip install django

   c) Desactivar el entorno:
          deactivate


► En Windows (CMD):

       nombre_del_entorno\Scripts\activate.bat


► En macOS / Linux:

       source nombre_del_entorno/bin/activate


-------------------------------------------------------------------------------
NOTAS IMPORTANTES
-------------------------------------------------------------------------------
• Todo paquete instalado dentro del entorno virtual queda aislado del sistema.  
• Verás el nombre del entorno al inicio de la línea de comandos cuando esté activo.  
• Puedes tener tantos entornos virtuales como proyectos.  
• Para eliminar un entorno basta con borrar su carpeta.
"""