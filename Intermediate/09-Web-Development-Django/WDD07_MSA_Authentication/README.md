# Django REST Authentication & CRUD Microservice

Este proyecto es un microservicio robusto construido con **Django REST Framework (DRF)**. Proporciona un sistema completo de autenticación basado en **JSON Web Tokens (JWT)**, una API RESTful para la gestión de un catálogo de productos y documentación interactiva auto-generada. Está preparado para ser consumido por aplicaciones frontend modernas gracias a su configuración de CORS.

## Características Principales

- **Autenticación JWT:** Endpoints seguros para obtener y refrescar tokens de acceso.
- **Registro de Usuarios:** Creación segura de cuentas.
- **CRUD de Productos:** Operaciones completas (Crear, Leer, Actualizar, Eliminar) con validaciones.
- **Filtros y Búsqueda:** Búsqueda por nombre, filtro por stock y ordenamiento.
- **Documentación Interactiva:** Interfaz Swagger UI y ReDoc integradas (vía `drf-spectacular`).
- **CORS Configurado:** Listo para integrarse con clientes externos (React, Angular, Vue, etc.).

## Tecnologías Utilizadas

- Python 3.x
- Django 6.0
- Django REST Framework (DRF)
- SimpleJWT (Autenticación)
- Django Filter (Filtros)
- drf-spectacular (OpenAPI 3 / Swagger)
- django-cors-headers (Seguridad CORS)
- SQLite3 (Base de datos)

## Instalación y Configuración Local

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd WDD07_MSA_Authentication
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto y añade:
```bash
DJANGO_SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
```

### 5. Migraciones y Ejecución
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Documentación y Endpoints de la API
Una vez que el servidor esté corriendo, puedes explorar e interactuar con toda la API gráficamente accediendo a:

- **Swagger UI (Recomendado para pruebas):** http://127.0.0.1:8000/api/docs/swagger/

### Resumen de Rutas Principales
#### Autenticación
- ```POST api/register/``` - Registra un usuario nuevo.
- ```POST api/token/``` - Obtiene access y refresh tokens (Login).
- ```POST api/token/refresh/``` - Refresca el token.

#### Productos (Requieren Header: ```Authorization: Bearer <access_token>```)
- ```GET /api/productos/``` - Lista productos (Soporta ```?search=```, ```?stock=```, ```?ordering=```).
- ```POST /api/productos/``` - Crea producto.
- ```GET, PUT, PATCH, DELETE /api/producto/<id>/``` - Gestión individual de un producto.

## Cómo hacer pruebas (Autenticación)
1. Ve a ```/api/register/``` y crea un usuario.
2. Ve a ```/api/token/``` y envía tus credenciales para obtener el token de acceso.
3. Copia el valor del ```access``` token.
4. En Swagger UI, haz clic en el botón Authorize en la parte superior y pega el token. A partir de ese momento, podrás usar las rutas protegidas de productos.