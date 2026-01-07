"""
==================================================
     EJERCICIO PRÁCTICO: GESTOR DE INVENTARIO
==================================================

Este ejercicio refuerza:
- Uso de clases y objetos
- Encapsulación de datos
- Manejo de diccionarios
- Interacción por consola
"""

# ==================================================
#                   CLASE PRODUCT
# ==================================================

class Product:
    """
    Representa un producto dentro del inventario.
    """
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def update_quantity(self, quantity):
        self.quantity = quantity
        
    def update_price(self, price):
        self.price = price
    
    def __str__(self):
        return (
            f"Producto: {self.name} | "
            f"Cantidad: {self.quantity} | "
            f"Precio: ${self.price:.2f}"
        )

# ==================================================
#               CLASE INVENTORY MANAGER
# ==================================================
    
class InventoryManager:
    """
    Administra el inventario de productos.
    """
    
    def __init__(self):
        self.inventory = {}
        
    def add_product(self, name, quantity, price):
        if name in self.inventory:
            print(
                f"El producto '{name}' ya existe. "
                "Actualizando cantidad y precio."
            )
            self.inventory[name].update_quantity(quantity)
            self.inventory[name].update_price(price)
        else:
            self.inventory[name] = Product(name, quantity, price)
            print(f"Producto '{name}' agregado al inventario.")
    
    def list_products(self):
        if not self.inventory:
            print("El inventario está vacío.")
            return
        
        print("\nLista de productos en el inventario:")
        for product in self.inventory.values():
            print(product)
            
    def search_product(self, name):
        if name in self.inventory:
            print(self.inventory[name])
        else:
            print(f"El producto '{name}' no se encontró en el inventario.")
    
    def update_product(self, name, quantity = None, price = None):
        product = self.inventory.get(name)
        if not product:
            print(f"El producto '{name}' no existe en el inventario.")
            return

        if quantity is not None:
            product.update_quantity(quantity)
            print(f"Cantidad de '{name}' actualizada a {quantity}.")

        if price is not None:
            product.update_price(price)
            print(f"Precio de '{name}' actualizado a ${price:.2f}.")
    
    def delete_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Producto '{name}' eliminado del inventario.")
        else:
            print(f"El producto '{name}' no existe en el inventario.")
    
    def start(self):
        while True:
            print("\nGestor de inventario")
            print("1. Agregar producto")
            print("2. Listar productos")
            print("3. Buscar producto")
            print("4. Actualizar producto")
            print("5. Eliminar producto")
            print("6. Salir")
            
            choice = input("Seleccione una opción: ").strip()
            
            if choice == "1":
                name = input("Nombre del producto: ").strip()
                try:
                    quantity = int(input("Cantidad: ").strip())
                    price = float(input("Precio: ").strip())
                    self.add_product(name, quantity, price)
                except ValueError:
                    print("Ingrese valores numéricos válidos para cantidad y precio.")
            elif choice == "2":
                self.list_products()
            elif choice == "3":
                name = input("Nombre del producto a buscar: ").strip()
                self.search_product(name)
            elif choice == "4":
                name = input("Nombre del producto a actualizar: ").strip()
                try:
                    quantity = input("Nueva cantidad (Enter para omitir): ").strip()
                    price = input("Nuevo precio (Enter para omitir): ").strip()

                    quantity = int(quantity) if quantity else None
                    price = float(price) if price else None

                    self.update_product(name, quantity, price)
                except ValueError:
                    print("Ingrese valores numéricos válidos.")
            elif choice == "5":
                name = input("Nombre del producto a eliminar: ").strip()
                self.delete_product(name)
            elif choice == "6":
                print("Saliendo del gestor de inventario...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

# ==================================================
#                 EJECUCIÓN PRINCIPAL
# ==================================================

if __name__ == "__main__":
    inventory_manager = InventoryManager()
    inventory_manager.start()