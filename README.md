# ASCEND - Plataforma de Red Privada

Arquitectura backend diseñada para una plataforma de red privada escalable, con un fuerte enfoque en el modelado de datos relacionales y la seguridad en la autenticación.

## 🛠 Stack Tecnológico
- **Lenguaje:** Python 3.13
- **Framework:** Django & Django REST Framework (DRF)
- **Base de Datos:** PostgreSQL
- **Arquitectura:** RESTful API

## 📌 Características Principales
- **Modelado de Datos:** Esquemas relacionales robustos para gestionar usuarios, perfiles y conexiones de red.
- **Seguridad:** Implementación de lógica de autenticación personalizada utilizando `AbstractUser`.
- **Escalabilidad:** Diseño orientado a evitar redundancias y asegurar la integridad referencial de los datos.

## ⚙️ Estructura del Backend
El proyecto se centra en tres pilares fundamentales:
1. **CustomUser:** Extensión del modelo de usuario base para adaptar la autenticación a las necesidades de la red.
2. **UserProfile:** Relación 1:1 para separar la lógica de autenticación de la información del perfil detallado.
3. **NetworkConnection:** Gestión de relaciones "Muchos a Muchos" con estados personalizados (Pendiente, Aceptada, Bloqueado).

---
*Desarrollado para demostrar buenas prácticas en modelado de esquemas y arquitectura de APIs en Django.*

## Estado del repositorio

Este repositorio contiene el núcleo de dominio de ASCEND: modelos Django, serializadores DRF y viewsets protegidos. Para ejecutarlo dentro de una aplicación Django se debe integrar el módulo en un proyecto con `AUTH_USER_MODEL` configurado y ejecutar migraciones.

## Dependencias

```bash
pip install -r requirements.txt
```

Las dependencias incluyen Django, Django REST Framework y el driver de PostgreSQL. No se incluyen credenciales ni datos de usuarios.
