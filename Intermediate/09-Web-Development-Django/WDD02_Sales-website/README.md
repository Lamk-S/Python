# 🛒 Sistema de Ventas - Django + PostgreSQL

Sistema web de ventas desarrollado con **Django**, conectado a una base de datos relacional **PostgreSQL**.  
El proyecto permite gestionar productos, clientes y ventas.

---

## 🚀 Tecnologías Utilizadas

- Python 3.x
- Django 6.x
- PostgreSQL
- HTML5 / CSS3
- Pillow (para manejo de imágenes)
- psycopg2 (adaptador PostgreSQL)

---

## 🏗 Creación inicial del Proyecto

Los siguientes comandos fueron utilizados para la configuración inicial del proyecto:

```bash
pip install django
pip install psycopg2
cd .\Intermediate\09-Web-Development-Django\
django-admin startproject sales_system
# Renombrado del directorio:
# Intermediate\09-Web-Development-Django\WDD01_Product-manager
python manage.py startapp core
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 Seguridad

- La `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`,`DB_HOST`,`DB_PORT` se gestiona mediante variable de entorno.
- El archivo `.env` (si se utiliza) no se encuentra versionado.