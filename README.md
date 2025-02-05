# 📄 Proyecto: Prueba Técnica - Gestión de Usuarios

Este proyecto es una solución para la gestión de usuarios, implementando un backend con **FastAPI** y **MySQL** como base de datos. Incluye pruebas automatizadas para garantizar el correcto funcionamiento del sistema.

---

## 🚀 Características

- **Gestión de Usuarios**:
  - Crear usuarios con validaciones específicas.
  - Evitar duplicidad de correos electrónicos.
- **Middleware**:
  - Registro de solicitudes y respuestas en los logs.
- **Pruebas**:
  - Casos de prueba automatizados para endpoints y middleware.
- **Código Modular**:
  - Separación de responsabilidades en controladores, modelos, servicios, middlewares y pruebas.

---

## 🛠️ Requisitos

- **Python** 3.10+
- **MySQL** instalado y configurado
- Dependencias del proyecto (ver `requirements.txt`)

---

## ⚙️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-repositorio/prueba-tecnica.git
   cd prueba-tecnica

2. **Configura el entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # En Linux/MacOS
    venv\Scripts\activate      # En Windows
3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
4. **Crea la base de datos:**
    
    Asegúrate de que MySQL esté ejecutándose.
    Crea una base de datos llamada db:
    ```bash
    CREATE DATABASE db;
5. **Configura el archivo .env: Crea un archivo .env en la raíz del proyecto y agrega las credenciales de tu base de datos:**

    ```bash
    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_NAME=db

Ejecuta las migraciones: Las tablas se crean automáticamente al iniciar el servidor.

▶️ Ejecución
Inicia el servidor:

    uvicorn main:app --reload
Accede a la documentación interactiva:

Visita http://127.0.0.1:8000/docs para explorar y probar los endpoints.
🧪 Pruebas
Ejecuta todas las pruebas:

    pytest
Resultados esperados: Deberías ver algo como:

    tests/test_usuarios.py .... [100%]
    tests/test_middleware.py .  [100%]
📂 Estructura del Proyecto

    📦 Prueba Tecnica
    ├── controllers
    │   └── usuarios_controller.py  # Controlador para manejar rutas relacionadas con usuarios
    ├── database
    │   ├── connection.py           # Configuración de conexión a la base de datos
    │   └── init_db.py              # Lógica de inicialización de la base de datos
    ├── middleware
    │   └── middleware.py           # Middleware para registrar solicitudes y respuestas
    ├── models
    │   └── usuario_model.py        # Modelo de base de datos para los usuarios
    ├── services
    │   └── usuario_service.py      # Lógica de negocio para manejar usuarios
    ├── tests
    │   ├── test_usuarios.py        # Pruebas de endpoints de usuarios
    │   └── test_middleware.py      # Pruebas para el middleware
    ├── main.py                     # Punto de entrada de la aplicación
    ├── .env                        # Archivo de configuración (ignorado por git)
    ├── requirements.txt            # Dependencias del proyecto
    └── README.md                   # Documentación del proyecto
    🛡️ Middleware
El middleware implementado registra información sobre cada solicitud y respuesta:

Método HTTP
URL
Código de estado de la respuesta
Puedes encontrarlo en middleware/middleware.py.

✨ Mejoras Futuras
Implementar autenticación y autorización (por ejemplo, JWT).
Agregar más validaciones en el backend.
Crear un frontend para interactuar con la API.
Optimizar consultas a la base de datos.