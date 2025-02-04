from models.usuario_model import Base
from database.connection import engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)
