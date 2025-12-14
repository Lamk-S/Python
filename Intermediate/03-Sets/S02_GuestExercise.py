# Conjunto de invitados
invitados = {"Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge", "Lucía"}

# Conjutno de invitados que han confirmado su asistencia
confirmados = {"Ana", "Carlos", "Sofía", "Lucía"}

# ----------------------------------------------------
# Invitados que han confirmado su asistencia
# ----------------------------------------------------
print("Invitados que han confirmado su asistencia:")
for invitado in confirmados:
    print(f"- {invitado} ha confirmado su asistencia.")

# ----------------------------------------------------
# Invitados que no han confirmado su asistencia
# ----------------------------------------------------
no_confirmados = invitados - confirmados
print("\nInvitados que NO han confirmado su asistencia:", no_confirmados)

# ----------------------------------------------------
# Todos los invitados (confirmados y no confirmados)
# ----------------------------------------------------
todos_invitados = confirmados | no_confirmados
print("Todos los invitados:", todos_invitados)

# ----------------------------------------------------
# Consulta interactiva (comentada para evitar pausas)
# ----------------------------------------------------
# invitado = input("Ingrese el nombre del invitado: ")
# if invitado in confirmados:
#     print(f"{invitado} ha confirmado su asistencia.")
# else:
#     print(f"{invitado} no ha confirmado su asistencia.")

# ----------------------------------------------------
# Copia del conjunto de invitados
# ----------------------------------------------------
copia_invitados = invitados.copy()
print("\nCopia del conjunto de invitados:", copia_invitados)

# ----------------------------------------------------
# Comprobaciones con issubset e isdisjoint
# ----------------------------------------------------
# issubset -> ¿Todos los invitados han confirmado?
print("¿Todos los invitados han confirmado?:", invitados.issubset(confirmados))

# issubset -> ¿Todos los confirmados están en la lista de invitados?
print("¿Todos los confirmados están en la lista de invitados?:", confirmados.issubset(invitados))

# isdisjoint -> ¿No existe ningún invitado confirmado?
print("¿No hay invitados confirmados?:", invitados.isdisjoint(confirmados))