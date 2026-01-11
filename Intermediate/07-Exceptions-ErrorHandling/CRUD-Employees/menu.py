from empleados import leer_empleados, crear_empleado, actualizar_empleado, eliminar_empleado

def mostrar_menu():
    while True:
        print("\n=====CRUD de Empelados=====")
        print("1. Leer todos los empleados")
        print("2. Crear nuevo empleado")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            leer_empleados()
        elif opcion == "2":
            crear_empleado()
        elif opcion == "3":
            actualizar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            print("Saliendo del Programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")