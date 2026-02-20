# WDD01_Product-manager

Aplicación web desarrollada con Django que implementa un gestor básico de productos con renderizado dinámico y manejo de archivos estáticos.

---

## 🚀 Tecnologías Utilizadas

- Python 3.x
- Django
- HTML5
- CSS3

---

## 🏗 Creación inicial del Proyecto

Los siguientes comandos fueron utilizados para la configuración inicial del proyecto:

```bash
pip install django
cd .\Intermediate\09-Web-Development-Django\
django-admin startproject product_manager
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp core
# Renombrado del directorio:
# Intermediate\09-Web-Development-Django\WDD01_Product-manager
python manage.py runserver
```

---

## 📁 Estructura del Proyecto

```
WDD01_Product-manager/
│
├── core/
│   ├── templates/
│   │   ├── base.html
│   │   ├── details.html
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   ├── products/
│
├── product_manager/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🔐 Seguridad

- La `SECRET_KEY` se gestiona mediante variable de entorno.
- El archivo `.env` (si se utiliza) no se encuentra versionado.
- La base de datos SQLite no se incluye en el repositorio.

---

## 📌 Estado del Proyecto

Versión inicial en desarrollo:
- Renderizado dinámico de productos.
- Manejo de archivos estáticos.
- Estructura base modular en Django.
