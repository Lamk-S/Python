CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE autores(
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

CREATE TABLE categorias(
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE editoriales(
    id_editorial INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    ciudad VARCHAR(50)
);

CREATE TABLE libros(
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    anio INT,
    isbn VARCHAR(20),
    id_autor INT,
    id_categoria INT,
    id_editorial INT,

    FOREIGN KEY(id_autor)
        REFERENCES autores(id_autor),

    FOREIGN KEY(id_categoria)
        REFERENCES categorias(id_categoria),

    FOREIGN KEY(id_editorial)
        REFERENCES editoriales(id_editorial)
);

CREATE TABLE usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    correo VARCHAR(120),
    telefono VARCHAR(20)
);

CREATE TABLE prestamos(
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    estado VARCHAR(20),

    FOREIGN KEY(id_usuario)
        REFERENCES usuarios(id_usuario),

    FOREIGN KEY(id_libro)
        REFERENCES libros(id_libro)
);

INSERT INTO autores(nombre,nacionalidad)
VALUES
('Gabriel García Márquez','Colombia'),
('Mario Vargas Llosa','Perú'),
('Isabel Allende','Chile'),
('Julio Verne','Francia'),
('George Orwell','Reino Unido');

INSERT INTO categorias(nombre)
VALUES
('Novela'),
('Ciencia Ficción'),
('Historia'),
('Fantasía'),
('Política');

INSERT INTO editoriales(nombre,ciudad)
VALUES
('Planeta','Barcelona'),
('Alfaguara','Madrid'),
('Penguin Random House','Lima');

INSERT INTO libros
(titulo,anio,isbn,id_autor,id_categoria,id_editorial)
VALUES
('Cien años de soledad',1967,'9780307474728',1,1,1),
('El amor en los tiempos del cólera',1985,'9780307389732',1,1,1),
('La ciudad y los perros',1963,'9788420471839',2,1,2),
('La casa de los espíritus',1982,'9788401352836',3,1,2),
('Viaje al centro de la Tierra',1864,'9788491050297',4,2,3),
('1984',1949,'9780451524935',5,5,3),
('Rebelión en la granja',1945,'9780451526342',5,5,3);

INSERT INTO usuarios
(nombres,correo,telefono)
VALUES
('Ana Torres','ana@gmail.com','999111222'),
('Luis Pérez','luis@gmail.com','988777666'),
('María López','maria@gmail.com','955444333'),
('Carlos Ruiz','carlos@gmail.com','977888111'),
('José Ramírez','jose@gmail.com','966555444');

INSERT INTO prestamos
(id_usuario,id_libro,fecha_prestamo,fecha_devolucion,estado)
VALUES
(1,1,'2025-01-10','2025-01-20','Devuelto'),
(2,3,'2025-02-05','2025-02-15','Devuelto'),
(3,6,'2025-03-01',NULL,'Prestado'),
(1,5,'2025-03-12','2025-03-20','Devuelto'),
(4,2,'2025-04-08',NULL,'Prestado'),
(5,7,'2025-04-20','2025-05-01','Devuelto');