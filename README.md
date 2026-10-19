# Apuntes del Curso de Python

Repositorio personal donde documento mi proceso de aprendizaje de Python, desde fundamentos hasta desarrollo de aplicaciones. Contiene apuntes teóricos, ejemplos de código y ejercicios prácticos organizados por niveles de dificultad.

Este repositorio sirve como material de estudio, consulta y como base para futuros proyectos.

## Objetivo del repositorio

- Consolidar bases sólidas de Python y buenas prácticas de programación.
- Mantener un historial ordenado y versionado de mi progreso.
- Crear un recurso reutilizable para consulta y práctica.
- Evolucionar de scripts básicos a proyectos completos.

## Estructura del repositorio

```
Python/
├── Basic/              # Fundamentos del lenguaje
├── Intermediate/       # Programación intermedia y proyectos
├── Advanced/           # Temas avanzados y arquitecturas
├── requirements.txt    # Dependencias (si aplica)
└── README.md
```

## Contenido por niveles

### 1. Basic
Enfocado en la sintaxis y lógica base de Python.
- Tipos de datos, variables y operadores
- Estructuras de control: condicionales y bucles
- Funciones y alcance
- Estructuras de datos: listas, tuplas, diccionarios, sets
- Manejo básico de errores

### 2. Intermediate
Enfocado en escritura de código limpio, modular y reutilizable.
- Programación Orientada a Objetos (POO)
- Módulos y paquetes
- Manejo de archivos y excepciones avanzadas
- Entornos virtuales y gestión de dependencias
- Principios SOLID y buenas prácticas
- Desarrollo Web con Django (MVT, Forms, Auth, Email, Security)
- Creación y publicación de paquetes en PyPI con setuptools, wheel y twine

### 3. Advanced
Enfocado en rendimiento, arquitectura y herramientas de producción.
- Programación funcional y decoradores avanzados
- Concurrencia, threading y async
- Testing y debugging
- Bases de datos y ORMs
- APIs REST
- Optimización y profiling

## Requisitos

- Python 3.10 o superior
- VS Code (recomendado)
- Git

Para los proyectos de Django:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Instalación y uso

1. Clona el repositorio:
```bash
git clone https://github.com/Lamk-S/Python.git
cd Python
```

2. Navega al nivel o proyecto que quieres revisar:
```bash
cd Basic/01-Variables
python ejemplo.py
```

Cada carpeta contiene su propio README con instrucciones específicas cuando es necesario.

## Convenciones

- Cada tema tiene su carpeta numerada para mantener el orden cronológico.
- El código está comentado con el objetivo de explicar el porqué, no solo el qué.
- Se prioriza la legibilidad sobre la complejidad innecesaria.

## Estado del proyecto

En desarrollo activo. El repositorio se actualiza conforme avanzo en el curso. Actualmente se está trabajando en los módulos de nivel intermedio.

Roadmap:
- [x] Fundamentos básicos completados
- [ ] Finalizar nivel intermedio (Django y empaquetado)
- [ ] Iniciar nivel avanzado
- [ ] Añadir tests unitarios a los ejercicios principales

## Autor

**Lamk-S**
GitHub: https://github.com/Lamk-S

## Licencia

Este proyecto se distribuye bajo licencia MIT. Libre para uso educativo y personal.
