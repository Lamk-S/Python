"""
==================================================
        Sistema de Seguridad con Tkinter
==================================================

Este ejercicio integra:
- Interfaces gráficas con Tkinter
- Uso de Frames para múltiples pantallas
- Base de datos SQLite
- Registro y autenticación de usuarios
- Manejo de eventos y validaciones
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ==================================================
# Clase principal de la aplicación
# ==================================================
# Controla la interfaz gráfica, la navegación entre
# pantallas y la conexión con la base de datos.

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Seguridad")
        self.root.configure(bg="#f0f0f0")
        
        # ----------------------------------------------
        # Conexión a la base de datos
        # ----------------------------------------------
        # Se crea (si no existe) la base de datos
        # donde se almacenan los usuarios.
        
        self.conn = sqlite3.connect(
            "Intermediate/08-GUI-Tkinter/Practical-Exercises/PE02_users.db"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

        # Mostrar la pantalla inicial
        self.show_login_screen()
    
    # ==================================================
    # Base de datos
    # ==================================================
    
    def create_table(self):
        """
        Crea la tabla de usuarios si no existe.
        """
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL
                            )
                            """)
        self.conn.commit()
    
    # ==================================================
    # Pantalla de Login
    # ==================================================
    # Permite al usuario autenticarse o ir al registro.
    
    def show_login_screen(self):
        self.clear_screen()
        self.login_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.SOLID, padx=10, pady=10)
        self.login_frame.pack(padx=20, pady=20)
        
        tk.Label(self.login_frame, text="Iniciar Sesión", font=("Arial", 18), bg="white").grid(
            row=0, column=0, columnspan=2, pady=10
        )
        
        tk.Label(self.login_frame, text="Usuario", bg="white").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_login_username = tk.Entry(self.login_frame, width=30)
        self.entry_login_username.grid(row=1, column=1, pady=5)
        
        tk.Label(self.login_frame, text="Contraseña", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_login_password = tk.Entry(self.login_frame, show="*", width=30)
        self.entry_login_password.grid(row=2, column=1, pady=5)
        
        tk.Button(self.login_frame, text="Iniciar Sesión", command=self.login_user, bg="#007bff", fg="white", width=15).grid(
            row=4, column=0, columnspan=2, pady=10
        )
        
        tk.Button(self.login_frame, text="Registrarse", command=self.show_register_screen, bg="#28a745", fg="white", width=15).grid(
            row=6, column=0, columnspan=2, pady=10
        )
    
    # ==================================================
    # Pantalla de Registro
    # ==================================================
    # Permite crear un nuevo usuario en la base de datos.
        
    def show_register_screen(self):
        self.clear_screen()
        
        self.register_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.SOLID, padx=10, pady=10)
        self.register_frame.pack(padx=20, pady=20)
        
        tk.Label(self.register_frame, text="Registrar Usuario", font=("Arial", 18), bg="white").grid(
            row=0, column=0, columnspan=2, pady=10
        )
        
        tk.Label(self.register_frame, text="Usuario", bg="white").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_register_username = tk.Entry(self.register_frame, width=30)
        self.entry_register_username.grid(row=1, column=1, pady=5)
        
        tk.Label(self.register_frame, text="Contraseña", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_register_password = tk.Entry(self.register_frame, show="*", width=30)
        self.entry_register_password.grid(row=2, column=1, pady=5)
        
        tk.Label(self.register_frame, text="Confirmar Contraseña", bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_register_cpassword = tk.Entry(self.register_frame, show="*", width=30)
        self.entry_register_cpassword.grid(row=3, column=1, pady=5)
        
        tk.Button(self.register_frame, text="Registrarse", command=self.register_user, bg="#007bff", fg="white", width=15).grid(
            row=5, column=0, columnspan=2, pady=10
        )
        
        tk.Button(self.register_frame, text="Volver", command=self.show_login_screen, bg="#a82b2b", fg="white", width=15).grid(
            row=6, column=0, columnspan=2, pady=10
        )
    
    # ==================================================
    # Utilidades
    # ==================================================
    
    def clear_screen(self):
        """
        Elimina todos los widgets actuales
        para cambiar de pantalla.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
            
    # ==================================================
    # Lógica
    # ==================================================
    
    def register_user(self):
        """
        Registra un nuevo usuario en la base de datos.
        """
        username = self.entry_register_username.get()
        password = self.entry_register_password.get()
        confirm_password = self.entry_register_cpassword.get()
        
        if not username or not password or not confirm_password:
            messagebox.showwarning("Advertencia", "Todos los datos son obligatorios.")
            return
        
        if password != confirm_password:
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden.")
            return
        
        try:
            self.cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Registro exitoso.")
            self.show_login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El nombre del usuario ya existe.")
    
    def login_user(self):
        """
        Valida las credenciales del usuario.
        """
        username = self.entry_login_username.get()
        password = self.entry_login_password.get()
        
        if not username or not password:
            messagebox.showwarning("Advertencia", "Todos los datos son obligatorios.")
            return
        
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        if user:
            messagebox.showinfo("Éxito", f"Bienvenido {username}!")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas!")
            
    def __del__(self):
        """
        Cierra la conexión a la base de datos
        al finalizar la aplicación.
        """
        self.conn.close()

# ==================================================
# Punto de entrada del programa
# ==================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()