from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from services.usuario_service import crear_usuario

router = APIRouter()

@router.post("/api/usuarios/crear")
def crear_usuario_endpoint(nombre: str, correo: str, rol: str, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = crear_usuario(db, nombre, correo, rol)
        return {"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
