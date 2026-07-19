CREATE DATABASE IF NOT EXISTS RestauranteDB;
USE RestauranteDB;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    telefono VARCHAR(20)
);

CREATE TABLE mesas (
    id_mesa INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL UNIQUE,
    capacidad INT NOT NULL,
    estado ENUM('Libre','Ocupada','Reservada') DEFAULT 'Libre'
);

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE platos (
    id_plato INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(8,2) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_cliente INT,
    id_empleado INT,
    id_mesa INT,
    estado ENUM('Pendiente','Preparando','Servido','Pagado') DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    FOREIGN KEY (id_mesa) REFERENCES mesas(id_mesa)
);

CREATE TABLE detalle_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_plato INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(8,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_plato) REFERENCES platos(id_plato)
);

CREATE TABLE pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
    metodo ENUM('Efectivo','Tarjeta','Yape','Plin'),
    total DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

-- ===========================
-- INSERCIÓN DE DATOS (MÁS REGISTROS)
-- ===========================

INSERT INTO clientes(nombre,telefono,correo) VALUES
('Juan Pérez','987654321','juan@gmail.com'),
('María López','999888777','maria@gmail.com'),
('Carlos Díaz','955444333','carlos@gmail.com'),
('Lucía Fernandez','933222111','lucia@gmail.com'),
('Roberto Gómez','922333444','roberto@gmail.com'),
('Ana Martínez','911222333','ana@gmail.com'),
('Diego Salinas','999000111','diego@gmail.com');

INSERT INTO empleados(nombre,cargo,telefono) VALUES
('Luis Torres','Mesero','988111111'),
('Ana Flores','Mesera','977222222'),
('José Rojas','Administrador','966333333'),
('Miguel Arce','Mesero','955666777'),
('Sofía Castro','Cajera','944555666');

INSERT INTO mesas(numero,capacidad,estado) VALUES
(1,4,'Libre'), (2,2,'Ocupada'), (3,6,'Libre'), (4,8,'Reservada'),
(5,4,'Libre'), (6,2,'Libre'), (7,4,'Ocupada'), (8,10,'Libre');

INSERT INTO categorias(nombre) VALUES
('Entradas'), ('Platos Fuertes'), ('Bebidas'), ('Postres'), ('Sopas');

INSERT INTO platos(nombre,descripcion,precio,id_categoria) VALUES
('Ceviche','Pescado fresco con limón',35.00,2),
('Lomo Saltado','Carne con papas fritas',42.00,2),
('Ají de Gallina','Pollo deshilachado',30.00,2),
('Arroz con Pato','Plato norteño',45.00,2),
('Tequeños','Rellenos de queso con guacamole',15.00,1),
('Papa a la Huancaína','Salsa de ají amarillo',18.00,1),
('Inca Kola','Gaseosa 500ml',6.50,3),
('Chicha Morada','Bebida tradicional 1L',12.00,3),
('Limonada Frozen','Jarra de limonada',15.00,3),
('Suspiro Limeño','Postre peruano',14.00,4),
('Torta de Chocolate','Porción',12.00,4),
('Sopa a la Minuta','Sopa de carne',22.00,5);

-- Simulamos pedidos en diferentes fechas
INSERT INTO pedidos(fecha,id_cliente,id_empleado,id_mesa,estado) VALUES
('2026-02-01 13:00:00',1,1,2,'Pagado'),
('2026-02-01 14:30:00',2,2,4,'Pagado'),
('2026-02-02 12:45:00',3,1,3,'Pagado'),
('2026-02-02 19:00:00',4,4,7,'Pagado'),
('2026-02-03 13:15:00',5,2,1,'Pagado'),
('2026-02-03 20:00:00',1,1,5,'Pagado'),
('2026-02-04 14:00:00',6,4,2,'Pagado'),
('2026-02-04 21:00:00',7,2,8,'Pagado');

INSERT INTO detalle_pedido(id_pedido,id_plato,cantidad,precio_unitario) VALUES
(1,1,2,35.00), (1,7,2,6.50), (1,10,1,14.00),
(2,2,1,42.00), (2,4,1,45.00), (2,8,1,12.00),
(3,3,2,30.00), (3,9,1,15.00),
(4,1,1,35.00), (4,2,1,42.00), (4,7,2,6.50), (4,11,2,12.00),
(5,5,1,15.00), (5,4,2,45.00), (5,8,1,12.00),
(6,12,2,22.00), (6,3,1,30.00), (6,7,3,6.50),
(7,6,1,18.00), (7,2,2,42.00), (7,9,1,15.00),
(8,1,3,35.00), (8,4,3,45.00), (8,8,2,12.00), (8,10,3,14.00);

INSERT INTO pagos(id_pedido,fecha_pago,metodo,total) VALUES
(1,'2026-02-01 14:00:00','Tarjeta',97.00),
(2,'2026-02-01 15:30:00','Yape',99.00),
(3,'2026-02-02 13:45:00','Efectivo',75.00),
(4,'2026-02-02 20:30:00','Tarjeta',114.00),
(5,'2026-02-03 14:30:00','Plin',117.00),
(6,'2026-02-03 21:15:00','Yape',93.50),
(7,'2026-02-04 15:00:00','Tarjeta',117.00),
(8,'2026-02-04 22:30:00','Tarjeta',306.00);