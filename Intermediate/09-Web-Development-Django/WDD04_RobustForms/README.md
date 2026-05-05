# 🛡️ RobustForms — Sistema de Validación y Manejo de Errores en Django

## 📌 Descripción

**RobustForms** es un proyecto desarrollado con Django enfocado en la implementación de **formularios robustos**, validaciones avanzadas del lado del servidor y manejo eficiente de errores. 

El proyecto simula una pasarela de pagos, demostrando cómo interceptar, sanitizar y validar datos sensibles (como tarjetas de crédito) antes de que toquen la base de datos, aplicando principios de arquitectura limpia y una excelente Experiencia de Usuario (UX) sin depender de pesados frameworks frontend.

## ✨ Características Principales

*   **Validación Multinivel en Django:** Uso de validadores integrados, métodos `clean_<field>()` para reglas de negocio específicas y `clean()` para validaciones cruzadas.
*   **Patrón Post/Redirect/Get (PRG):** Prevención de reenvío de formularios dobles tras un cobro exitoso.
*   **Seguridad de Datos:** Almacenamiento exclusivo de metadatos no sensibles (últimos 4 dígitos) simulando flujos reales de Fintech.
*   **Interfaz Dinámica (Vanilla JS & CSS):** Renderizado de una tarjeta de crédito 3D que reacciona en tiempo real a los inputs del usuario (formateo automático, giro para CVV, detección de franquicia).
*   **Feedback Inmediato:** Integración del sistema de `Messages` de Django y renderizado manual de errores por campo para una UX fluida.

## ⚙️ Tecnologías Utilizadas

*   **Backend:** Python 3.x, Django
*   **Base de Datos:** SQLite
*   **Frontend:** HTML5, CSS3 avanzado (Animaciones 3D), Vanilla JavaScript, Bootstrap 5 (UI components)