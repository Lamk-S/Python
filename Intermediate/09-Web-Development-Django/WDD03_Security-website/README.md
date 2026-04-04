# 🔐 Sistema de Autenticación - Django

Aplicación web desarrollada con **Django** que implementa un sistema de autenticación completo utilizando el sistema встроido de usuarios.

El proyecto permite el registro, inicio y cierre de sesión de usuarios, así como la gestión básica de autenticación.

---

## 🚀 Tecnologías Utilizadas

- Python 3.x  
- Django 6.x  
- SQLite / PostgreSQL (según configuración)  
- HTML5 / CSS3  

---

## 🏗 Creación del Proyecto

Comandos utilizados para la configuración inicial:

```bash
pip install django
cd .\Intermediate\09-Web-Development-Django\
django-admin startproject security_website
# Renombrado del directorio:
# Intermediate\09-Web-Development-Django\WDD03_Security-website
cd WDD03_Security-website
python manage.py startapp accounts
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver