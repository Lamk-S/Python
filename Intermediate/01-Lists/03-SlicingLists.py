"""
---------------------------------------------------------
Slicing en Python (rebanado de listas)
---------------------------------------------------------

Sintaxis básica:
lista[inicio:fin:paso]

Resumen de usos comunes:
- lista[inicio:fin]        -> Obtiene los elementos desde "inicio" hasta "fin - 1".
- lista[:fin]              -> Desde el inicio hasta "fin - 1".
- lista[inicio:]           -> Desde “inicio” hasta el final de la lista.
- lista[inicio:fin:paso]   -> Igual que el slicing básico, pero avanzando según "paso".
- lista[::-1]              -> Crea una copia invertida de la lista (atajo para invertir).
---------------------------------------------------------
"""

# Lista base
lista = [0, 1, 2, 3, 4, 5, 6]

# Slicing desde índice 2 hasta 4 (fin - 1)
sub_lista = lista[2:5]
print(sub_lista)  # [2, 3, 4]

# Slicing desde el inicio hasta índice 3 (fin - 1)
sub_lista2 = lista[:4]
print(sub_lista2)  # [0, 1, 2, 3]

# Slicing desde índice 4 hasta el final
sub_lista3 = lista[4:]
print(sub_lista3)  # [4, 5, 6]

# Slicing usando índices negativos
sub_lista4 = lista[-4:-1]  
print(sub_lista4)  # [3, 4, 5]

# Copia completa usando slicing
copia_completa = lista[:]
print(copia_completa)  # [0, 1, 2, 3, 4, 5, 6]

# Slicing con paso: desde 1 hasta 5 (fin - 1), saltando de 2 en 2
sub_lista_paso = lista[1:6:2]
print(sub_lista_paso)  # [1, 3, 5]

# Copia completa en orden inverso
copia_completa_reves = lista[::-1]
print(copia_completa_reves)  # [6, 5, 4, 3, 2, 1, 0]