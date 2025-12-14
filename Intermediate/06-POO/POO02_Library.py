"""
Este módulo simula un sistema básico de biblioteca utilizando
las clases Autor, Libro y Biblioteca.
"""

class Autor:
    """Representa a un autor de uno o más libros."""
    def __init__(self, nombre: str, fecha_nacimiento:str):
        if not isinstance(nombre, str):
            raise TypeError("El nombre del autor debe ser una cadena de texto.")
        if not isinstance(fecha_nacimiento, str):
            raise TypeError("La fecha de nacimiento debe ser una cadena (YYYY-MM-DD).")
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
    
    def __str__(self) -> str:
        return f"{self.nombre} (nacido el {self.fecha_nacimiento})"

class Libro:
    """Representa un libro dentro de la biblioteca."""
    def __init__(self, titulo: str, autor: Autor, año_publicacion: int):
        if not isinstance(titulo, str):
            raise TypeError("El título debe ser una cadena de texto.")
        if not isinstance(autor, Autor):
            raise TypeError("El autor debe ser una instancia de la clase Autor.")
        if not isinstance(año_publicacion, int):
            raise TypeError("El año de publicación debe ser un número entero.")

        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor} (Publicado en {self.año_publicacion})"

class Biblioteca:
    """Representa una biblioteca que contiene libros."""
    def __init__(self):
        self.libros=[]
        
    def agregar_libro(self, libro: Libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se pueden agregar instancias de la clase Libro.")
        
        self.libros.append(libro)
    
    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        """Busca libros por título (búsqueda parcial)."""
        return [
            libro for libro in self.libros
            if titulo.lower() in libro.titulo.lower()
        ]
    
    def buscar_por_autor(self, nombre_autor: str) -> list[Libro]:
        """Busca libros por nombre del autor (búsqueda parcial)."""
        return [
            libro for libro in self.libros
            if nombre_autor.lower() in libro.autor.nombre.lower()
        ]
    
    def eliminar_libro(self, titulo: str) -> bool:
        """Elimina un libro por su título."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                return True
        return False
    
    def mostrar_libros(self) -> str:
        if not self.libros:
            return "La Biblioteca esta vacía."
        return "\n".join(str(libro) for libro in self.libros)


# -----------------------------
# Ejemplo de uso del módulo
# -----------------------------

# Crear autores
autor1 = Autor("Gabriel García Márquez", "1927-03-06")
autor2 = Autor("Isabel Allende Llona", "1942-08-02")

# Crear libros
libro1 = Libro("Cien años de soledad", autor1, 1967)
libro2 = Libro("La casa de los espíritus", autor2, 1982)

# Crear biblioteca
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrar libros
print("Libros disponibles:")
print(biblioteca.mostrar_libros())

# Buscar libros
print("\nBúsqueda por título ('cien'):")
for libro in biblioteca.buscar_por_titulo("cien"):
    print(libro)

print("\nBúsqueda por autor ('allende'):")
for libro in biblioteca.buscar_por_autor("allende"):
    print(libro)

# Eliminar libro
print("\nEliminando 'Cien años de soledad'...")
eliminado = biblioteca.eliminar_libro("Cien años de soledad")
print("Libro eliminado." if eliminado else "Libro no encontrado.")

# Mostrar libros finales
print("\nLibros restantes:")
print(biblioteca.mostrar_libros())