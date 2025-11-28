"""
Sistema de Registro de Ventas

- Guarda cada venta (con detalles del producto, cantidad y precio) en un archivo de texto.
- Muestra un reporte en consola.
- Cada vez que se realiza una venta, se registra en el archivo "ventas.txt".
"""

def registrar_venta(producto, cantidad, precio):
    # Calcula el total de la venta
    total = cantidad * precio

    # Abre el archivo en modo 'a' (append) para no borrar lo anterior
    with open("Basic/File-Handling/ventas.txt", "a") as archivo:
        archivo.write(
            f"Producto: {producto}, Cantidad: {cantidad}, "
            f"Precio: {precio}, Total: {total}\n"
        )

    print(f"Venta registrada: {producto}, {cantidad} unidades, ${total:.2f} total")


# Ejemplos de uso
registrar_venta("Lápiz", 3, 0.50)
registrar_venta("Cuaderno", 2, 1.75)