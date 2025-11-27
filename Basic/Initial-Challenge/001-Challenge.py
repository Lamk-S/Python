# =====================================================
# 001.- Calcular el precio total de un producto con IGV
# =====================================================

# PRECIO_SIN_IGV = 100
# IGV = 0.18
# precio_con_igv = PRECIO_SIN_IGV * (1 + IGV)
# print(f"Precio con Igv: {precio_con_igv:.2f}")

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
total_a_pagar = precio_producto * cantidad_producto
igv_a_pagar = total_a_pagar * 0.18
total_neto = total_a_pagar + igv_a_pagar
print(f"El total a pagar a pagar por el producto es: {total_neto:.2f} el IGV es: {igv_a_pagar:.2f}")