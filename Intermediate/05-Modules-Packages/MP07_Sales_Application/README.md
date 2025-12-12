# Aplicación de Ventas

Este Paquete proporciona funcionalidaddes para gestionar ventas, incluyendo cálculos de precios, impuestos y descuentos.

---

## 🚀 Guía para publicar paquetes en PyPI usando Twine

Esta guía describe paso a paso cómo generar, verificar y publicar un paquete de Python en PyPI utilizando **setuptools**, **wheel** y **twine**.

---

### PASO 1 — Instalar herramientas necesarias

Para poder crear y publicar un paquete en PyPI necesitas instalar las siguientes herramientas:

- `setuptools` — Para empaquetar tu proyecto
- `wheel` — Para crear archivos binarios instalables
- `twine` — Para subir tu paquete a PyPI

#### Comando de instalación
```bash
pip install setuptools wheel twine
```

---

### PASO 2 — Generar la distribución del paquete

Una vez instaladas las herramientas, genera los archivos que permitirán instalar tu paquete:

```bash
python setup.py sdist bdist_wheel
```

---

### PASO 3 — Verificar archivos generados

Antes de subirlos, es importante comprobar que los archivos de distribución son válidos:

```bash
twine check dist/*
```

---

### PASO 4 — Subir el paquete a PyPI

Si todo está correcto, sube tu paquete al repositorio oficial de PyPI:

```bash
twine upload dist/*
```

---

### PASO 5 — Subir a PyPI de prueba

Antes de publicar oficialmente, puedes probar la publicación en TestPyPI:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

---

### PASO 6 — Instalar el paquete desde PyPI

Una vez publicado oficialmente, cualquier usuario puede instalar tu paquete con:

```bash
pip install sales_application_lamk_s
