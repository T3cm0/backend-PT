from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.usuarios_controller import router as usuarios_router
from models.usuario_model import Base
from database.connection import engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:4200",  # Permite solicitudes desde Angular
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Registrar el router
app.include_router(usuarios_router)
