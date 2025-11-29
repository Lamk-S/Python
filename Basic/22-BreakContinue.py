"""
Break y Continue en Bucles
--------------------------
break    -> Se utiliza para salir inmediatamente de un bucle.
continue -> Permite omitir el resto del código dentro del bucle y continuar 
            con la siguiente iteración.
"""

# Ejemplo 1: Uso de break en un bucle FOR
"""
for i in range(10):
    if i == 5:
        break  # El bucle se detiene cuando i es 5
    print(i)
"""

# Ejemplo 2: Uso de break en un bucle WHILE
"""
contador = 0
while True:
    if contador >= 5:
        break  # Salir del bucle cuando contador llegue a 5
    print(contador)
    contador += 1
"""

# Ejemplo 3: Uso de continue en un bucle FOR (imprime solo números impares)
"""
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar los números pares
    print(i)
"""

# Ejemplo 4: Uso de continue en un bucle WHILE (imprime solo números impares)
contador = 0

while contador < 10:
    if contador % 2 == 0:
        contador += 1
        continue  # Saltar la impresión si el número es par
    
    print(contador)
    contador += 1