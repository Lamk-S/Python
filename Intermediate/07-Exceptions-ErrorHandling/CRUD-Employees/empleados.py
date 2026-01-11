from database import conectar

def leer_empleados():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
            SELECT id, nombre, edad, puesto FROM empleados
            WHERE estado = 1
                   """)
    
    empleados = cursor.fetchall()
    
    if empleados:
        print("{:<5} {:<20} {:<15} {:<20}".format("ID", "NOMBRE", "EDAD", "PUESTO"))
        for emp in empleados:
            print("{:<5} {:<20} {:<15} {:<20}".format(emp[0], emp[1], emp[2], emp[3]))
    else:
        print("No hay empleados registrados.")
        
def crear_empleado():
    conn = conectar()
    cursor = conn.cursor()
    
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    puesto = input("Puesto del empleado: ")
    estado = 1
    cursor.execute("""
            INSERT INTO empleados (nombre, edad, puesto, estado)
            VALUES (?, ?, ?, ?)
                   """, (nombre, edad, puesto, estado))
    conn.commit()
    conn.close()
    print("Empleado agregado exitosamente.")

def actualizar_empleado():
    id_empleado = int(input("ID del empleado a actualizar: "))
    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
    nueva_edad = input("Nueva edad (dejar vacío para no cambiar): ")
    nuevo_puesto = input("Nuevo puesto (dejar vacío para no cambiar): ")
    
    conn = conectar()
    cursor = conn.cursor() 
    
    if nuevo_nombre:
        cursor.execute("UPDATE empleados SET nombre = ? WHERE id = ?", (nuevo_nombre, id_empleado))
    if nueva_edad:
        cursor.execute("UPDATE empleados SET edad = ? WHERE id = ?", (nueva_edad, id_empleado))
    if nuevo_puesto:
        cursor.execute("UPDATE empleados SET puesto = ? WHERE id = ?", (nuevo_puesto, id_empleado))
    
    conn.commit()
    conn.close()
    print("Empleado actualizado correctamente.")

def eliminar_empleado():
    id_empleado = int(input("ID del empleado a eliminar: "))
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE empleados SET estado = 0 WHERE id = ?", (id_empleado,))
    
    conn.commit()
    conn.close()
    print("Empleado eliminado correctamente.")