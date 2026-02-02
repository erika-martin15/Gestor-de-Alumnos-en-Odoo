# Gestor de Alumnos para Plaiaundi

Este repositorio contiene un módulo de gestión académica desarrollado para Odoo, diseñado específicamente para satisfacer las necesidades de administración de alumnos, profesores y recursos del centro Plaiaundi.

## Características Principales

El módulo permite una gestión integral de los siguientes elementos:

- **Expedientes Académicos**: Registro completo de alumnos, incluyendo información de contacto, asignación de ciclos y seguimiento académico.
- **Gestión Docente**: Administración de la plantilla de profesores y su vinculación con los distintos ciclos formativos.
- **Infraestructura Educativa**: Control de aulas y ciclos formativos (grados).
- **Control de Inventario**: Seguimiento detallado del equipamiento informático, su ubicación en las aulas y la asignación individual a los estudiantes.
- **Mantenimiento**: Sistema de registro de incidencias técnicas para el equipamiento del centro.
- **Seguimiento Académico**: Gestión de asistencias y calificaciones por evaluación.

## Estructura del Proyecto

El código está organizado siguiendo las mejores prácticas de desarrollo en Odoo, con una arquitectura modular y nombres técnicos en castellano para facilitar su mantenimiento.

- `models/`: Definición de la lógica de negocio y estructuras de datos.
- `views/`: Definición de las interfaces de usuario (formularios, listados y menús).
- `security/`: Reglas de acceso y permisos.
- `demo/`: Datos de ejemplo para pruebas.

## Instalación

1. Copie la carpeta `plaiaundi_management` dentro del directorio de `addons` de su instancia de Odoo.
2. Asegúrese de que el usuario del sistema tiene los permisos de lectura adecuados sobre el directorio.
3. Reinicie el servicio de Odoo.
4. Active el modo desarrollador en la interfaz web de Odoo.
5. Vaya al menú de Aplicaciones y pulse en "Actualizar lista de aplicaciones".
6. Busque "Plaiaundi Management" e instale el módulo.

## Requisitos

- Odoo 17.0, 18.0 o superior.
- Python 3.10 o superior.
