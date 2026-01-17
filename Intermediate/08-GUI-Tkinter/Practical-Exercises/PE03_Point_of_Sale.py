"""
==================================================
        Punto de Venta (POS) con Tkinter
==================================================

Este ejercicio integra:
- Interfaces gráficas complejas con Tkinter
- Uso de Frames para organizar la UI
- Base de datos SQLite
- Manejo de eventos
- Generación de tickets en PDF
- Separación entre lógica, datos y presentación
"""

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# ==================================================
# Clase principal de la aplicación
# ==================================================

class PointOfSaleApp:
    """
    Clase que representa un sistema básico de Punto de Venta (POS).
    Controla la interfaz, la base de datos y la lógica del negocio.
    """
    
    def __init__(self, master):
        # ----------------------------------------------
        # Configuración de la ventana principal
        # ----------------------------------------------
        self.master = master
        self.master.title("Sistema de Punto de Venta")
        self.master.geometry("1024x450")
        self.master.configure(bg="#e6e6e6")
        
        # Inicialización de base de datos y UI
        self.db_init()
        self.create_widgets()
    
    # ==================================================
    # Base de datos
    # ==================================================
    
    def db_init(self):
        """
        Inicializa la conexión a la base de datos y
        crea la tabla de productos si no existe.
        """
        try:
            self.db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "PE03_sales.db"
            )
            
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    cantidad INTEGER NOT NULL
                )
            """)
            self.conn.commit()
            
            # Insertar productos por defecto solo si la tabla está vacía
            self.cursor.execute("SELECT COUNT(*) FROM productos")
            if self.cursor.fetchone()[0] == 0:
                productos_default = [
                    ("Arroz 1Kg", 4.50, 100),
                    ("Azúcar 1Kg", 4.20, 80),
                    ("Aceite Vegetal 1L", 12.90, 60),
                    ("Leche Entera 1L", 3.80, 120),
                    ("Pan de Molde", 6.50, 40),
                    ("Huevos (Docena)", 9.90, 50),
                    ("Fideos 500g", 3.60, 90),
                    ("Gaseosa 1.5L", 7.50, 70)
                ]
                self.cursor.executemany(
                    "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
                    productos_default
                )
                self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error BD", f"No se pudo inicializar la BD:\n{e}")
            self.master.quit()
            
    def load_products(self):
        """
        Obtiene los nombres de los productos desde la BD
        para cargarlos en el Combobox.
        """
        self.cursor.execute("SELECT nombre FROM productos")
        return [fila[0] for fila in self.cursor.fetchall()]
    
    def update_stock(self, nombre, nuevo_stock):
        """
        Actualiza el stock de un producto tras una venta.
        """
        self.cursor.execute(
            "UPDATE productos SET cantidad = ? WHERE nombre = ?",
            (nuevo_stock, nombre)
        )
        self.conn.commit()
    
    # ==================================================
    # Lógica del carrito
    # ==================================================
    
    def add_products(self):
        """
        Agrega un producto al carrito (Treeview),
        valida stock y recalcula el total.
        """
        producto = self.combobox_producto.get()
        cantidad = self.entry_cantidad.get()
        
        if not producto or not cantidad:
            messagebox.showwarning("Advertencia", "Seleccione producto y cantidad.")
            return
        
        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero.")
            return
            
        self.cursor.execute("SELECT * FROM productos WHERE nombre = ?", (producto,))
        resultado = self.cursor.fetchone()
        
        if not resultado:
            return

        id_producto, nombre, precio, stock = resultado
        
        if cantidad > stock:
            messagebox.showwarning(
                "Stock insuficiente",
                f"Solo hay {stock} unidades disponibles."
            )
            return
        
        total = cantidad * precio
        self.tree.insert(
            "",
            tk.END,
            values=(id_producto, nombre, f"{precio:.2f}", cantidad, f"{total:.2f}")
        )
        
        self.update_stock(nombre, stock - cantidad)
        self.calculate_total()
        self.clear_fields()
                
    def calculate_total(self):
        """
        Recorre el carrito y calcula el total acumulado.
        """
        total = sum(
            float(self.tree.item(item, "values")[4])
            for item in self.tree.get_children()
        )
        self.label_total.config(text=f"Total: ${total:.2f}")
    
    def clear_fields(self):
        """
        Limpia los campos de entrada.
        """
        self.combobox_producto.set("")
        self.entry_cantidad.delete(0, tk.END)
        
    # ==================================================
    # Ticket en PDF
    # ==================================================
        
    def print_ticket(self):
        """
        Genera un ticket en PDF con los productos del carrito.
        """
        if not self.tree.get_children():
            messagebox.showwarning("Advertencia", "No hay productos en el carrito.")
            return
        
        pdf_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "PE03_ticket.pdf"
        )
        
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        
        c.drawString(30, 750, "Tienda XYZ - Ticket de compra")
        c.drawString(30, 735, "=" * 40)
        
        y = 710
        total_general = 0
        
        for item in self.tree.get_children():
            _, producto, precio, cantidad, total = self.tree.item(item, "values")
            total_general += float(total)

            c.drawString(30, y, producto)
            c.drawString(200, y, str(precio))
            c.drawString(300, y, str(cantidad))
            c.drawString(380, y, str(total))
            y -= 20
        
        c.drawString(30, y - 10, "=" * 40)
        c.drawString(250, y - 30, f"Total: $ {total_general:.2f}")
        
        c.save()
        os.startfile(pdf_path)

        messagebox.showinfo("Éxito", "Ticket generado correctamente.")
        
    # ==================================================
    # Interfaz gráfica (Frames)
    # ==================================================
    
    def create_product_frame(self):
        """
        Frame para selección de productos.
        """
        self.frame_productos = tk.Frame(self.master, bg="#007BFF", bd=2, relief="groove")
        self.frame_productos.place(x=20, y=20, width=300, height=200)
        
        label_producto_titulo = tk.Label(
            self.frame_productos, text="Agregar Producto", bg="#007BFF", fg="white",
            font=("Arial", 14, "bold")
        )
        label_producto_titulo.pack(pady=10)
        
        label_producto = tk.Label(self.frame_productos, text="Producto:", bg="#007BFF", 
            fg="white", font=("Arial", 12)
        )
        label_producto.pack()
        self.combobox_producto = ttk.Combobox(self.frame_productos, state="readonly", values=self.load_products())
        self.combobox_producto.pack(pady=5)
        
        label_cantidad = tk.Label(self.frame_productos, text="Cantidad:", bg="#007BFF", 
            fg="white", font=("Arial", 12)
        )
        label_cantidad.pack()
        self.entry_cantidad = ttk.Entry(self.frame_productos)
        self.entry_cantidad.pack(pady=5)
        
        btn_agregar = tk.Button(self.frame_productos, text="Agregar al carrito", command=self.add_products, bg="#28A745", fg="white")
        btn_agregar.pack(pady=5)
        
    def create_cart_frame(self):
        """
        Frame del carrito de compras.
        """
        self.frame_carrito = tk.Frame(self.master, bg="#ffffff", bd=2, relief="groove")
        self.frame_carrito.place(x=340, y=20, width=660, height=400)
        
        label_carrito_titulo = tk.Label(
            self.frame_carrito, text="Carrito de Compras", bg="#ffffff", fg="#000000",
            font=("Arial", 14, "bold")
        )
        label_carrito_titulo.pack(pady=10)
        
        columns = ("ID", "Producto", "Precio", "Cantidad", "Total")
        self.tree = ttk.Treeview(self.frame_carrito, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(padx=10, pady=10)
    
    def create_total_frame(self):
        """
        Frame que muestra el total y permite imprimir.
        """
        self.frame_total = tk.Frame(self.master, bg="#6C757D", bd=2, relief="groove")
        self.frame_total.place(x=20, y=230, width=300, height=190)
        
        label_total = tk.Label(
            self.frame_total, text="Total a Pagar", bg="#6C757D", fg="white",
            font=("Arial", 14, "bold")
        )
        label_total.pack(pady=10)
        
        self.label_total = tk.Label(self.frame_total, text="Total: $0.00", bg="#6C757D",
        fg="white", font=("Arial", 14, "bold")
        )
        self.label_total.pack(pady=20)
        
        btn_imprimir = tk.Button(self.frame_total, text="Imprimir Ticket", command=self.print_ticket, bg="#007BFF",
            fg="white"
        )
        btn_imprimir.pack(pady=10)
    
    def create_widgets(self):
        """
        Punto central de creación de la UI.
        """
        self.create_product_frame()
        self.create_cart_frame()
        self.create_total_frame()
    
    def __del__(self):
        self.conn.close()
        
# ==================================================
# Punto de entrada del programa
# ==================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = PointOfSaleApp(root)
    root.mainloop()