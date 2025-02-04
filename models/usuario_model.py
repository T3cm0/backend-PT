from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    rol = Column(String(50), nullable=False)
