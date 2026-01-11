SELECT * FROM empleados

--CRUD = 
--C = CREATE (INSERT)
--R = READ(SELECT)
--U = UPDATE(UPDATE)
--D = DELETE(DELETE)

INSERT INTO empleados (nombre, edad, puesto)
VALUES
("Juan Perez", 28, "Desarrollador"),
("María López", 24, "Analista"),
("Alfredo Lezcano", 25, "Gerente");

--Recuperar
SELECT * FROM empleados
WHERE edad >= 25;
--Actualizar
UPDATE empleados SET puesto = "Ingeniero Senior" WHERE id = 3;
UPDATE empleados SET estado = "1" WHERE id IN(1, 2)
UPDATE empleados SET estado = "0" WHERE id = 3
--Eliminar un registro
DELETE FROM empleados WHERE id = 1;
--Contar registros
SELECT COUNT(*) FROM empleados;
--Modificar la estructura de la tabla
ALTER TABLE empleados
ADD COLUMN estado char(1)
--Mostrar los empleados activos
SELECT * FROM empleados WHERE estado = 1
