"""
Módulo para generar códigos QR utilizando las librerías 'qrcode' y 'Pillow'.

Requisitos previos:
    pip install qrcode
    pip install Pillow

Este script permite generar un código QR a partir de un texto o URL
y guardarlo en un archivo de imagen PNG.
"""


import qrcode

def generar_codigo_qr(datos, nombre_archivo):
    """
    Genera un código QR con los datos proporcionados y lo guarda como un archivo de imagen.
    """
    # Configuración del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(datos)
    qr.make(fit = True)

    # Crear imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    # Guardar archivo
    img.save("Intermediate/05-Modules-Packages/" + nombre_archivo + ".png") 
    
    print(f"Código QR generado y guardado como '{nombre_archivo}.png'")

# Datos para el QR (se recomienda usar la URL completa)
datos_para_qr = "https://www.python.org"

# Nombre del archivo de salida
nombre_archivo_salida = "codigo_qr"

# Generar el código QR
generar_codigo_qr(datos_para_qr, nombre_archivo_salida)