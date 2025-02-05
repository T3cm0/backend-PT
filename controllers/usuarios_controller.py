from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from services.usuario_service import crear_usuario
from database.connection import get_db

# Crear el router para manejar las rutas de usuarios
router = APIRouter()

# Esquema Pydantic para validación de entrada
class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr  # Valida automáticamente que el correo sea válido
    rol: str

@router.post("/api/usuarios/crear")
def crear_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Endpoint para crear un nuevo usuario.

    Args:
        usuario (UsuarioCreate): Datos del usuario a crear.
        db (Session): Sesión de la base de datos.

    Returns:
        dict: Mensaje de éxito y datos del usuario creado.
    """
    try:
        # Llama al servicio para crear el usuario
        nuevo_usuario = crear_usuario(db, usuario.nombre, usuario.correo, usuario.rol)
        return {"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}
    except ValueError as e:
        # Maneja errores personalizados como correo duplicado
        raise HTTPException(status_code=400, detail=str(e))
