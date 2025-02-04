from fastapi import FastAPI
from controllers.usuarios_controller import router as usuarios_router
from models.usuario_model import Base
from database.connection import engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()

# Registrar el router
app.include_router(usuarios_router)
