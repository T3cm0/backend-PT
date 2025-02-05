from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base  # Actualizado para usar la importación recomendada

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    rol = Column(String(50), nullable=False)
