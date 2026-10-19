# Apuntes del Curso de Python

Repositorio personal donde documento mi proceso de aprendizaje de Python desde cero hasta desarrollo web y análisis de datos. Contiene apuntes teóricos, ejercicios prácticos, notebooks, GUIs y proyectos Django, organizados por niveles de dificultad.

Funciona como bitácora de aprendizaje, material de consulta y portafolio técnico.

## Objetivo del repositorio

- Consolidar fundamentos de Python con buenas prácticas y PEP8.
- Pasar de scripts básicos a código modular, POO y manejo de errores.
- Desarrollar interfaces gráficas y aplicaciones web con Django.
- Especializarse en análisis y visualización de datos con Pandas y Seaborn.
- Mantener un historial ordenado, versionado y reutilizable.

## Estructura del repositorio

```
Python/
├── Basic/
│   ├── 00-HelloWorld.py -> 22-BreakContinue.py (Fundamentos)
│   ├── Basic-Exercises/ (001 a 008 + ventas.csv)
│   ├── Break-Continue/
│   ├── Conditionals/
│   ├── File-Handling/
│   └── Initial-Challenge/
├── Intermediate/
│   ├── 01-Lists/
│   ├── 02-Tuples-Dictionaries/
│   ├── 03-Sets/
│   ├── 04-Functions/
│   ├── 05-Modules-Packages/
│   ├── 06-POO/
│   ├── 07-Exceptions-ErrorHandling/
│   ├── 08-GUI-Tkinter/
│   └── 09-Web-Development-Django/
├── Advanced/
│   ├── 01-Pandas/
│   ├── 02-Data-Manipulation/
│   ├── 03-Data-Import-Export/
│   ├── 04-Data-Visualization-With-Pandas/
│   └── 05-Matplotlib-And-Seaborn/
└── README.md
```

## Tecnologías y librerías

- **Lenguaje:** Python 3.10+
- **Fundamentos:** PEP8, manejo de archivos, lógica
- **Intermedio:** POO, Tkinter, Qt Designer, manejo de excepciones, SQLite
- **Web:** Django 6.x, python-dotenv
- **Datos:** Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy, PyMySQL, openpyxl
- **Herramientas:** VS Code, Jupyter Notebook, Git, venv, setuptools, wheel, twine, Colorama, qrcode

## Requisitos e instalación

1. Clonar:
```bash
git clone https://github.com/Lamk-S/Python.git
cd Python
```

2. Entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

## Convenciones del repositorio

- Carpetas numeradas para mantener orden cronológico de aprendizaje.
- Nomenclatura descriptiva: `L` para Listas, `TD` para Tuples/Dicts, `POO` para clases, `DM` para Data Manipulation, `DIE` para Import/Export, etc.
- Cada proyecto Django incluye su propio README con setup específico.
- Notebooks comentados explicando el porqué de cada transformación.

## Estado del proyecto

En desarrollo activo.

- [x] Basic - Fundamentos y 8 ejercicios completados
- [x] Intermediate - Listas a POO, GUI y 7 proyectos Django completados
- [x] Advanced - Pandas, manipulación, import/export y visualización en progreso
- [ ] Proyecto final integrador de análisis de datos + visualización
- [ ] Añadir tests y documentación docstring completa

## Autor

**Lamk-S**
GitHub: https://github.com/Lamk-S/Python

## Licencia

MIT. Uso libre para fines educativos y personales.
