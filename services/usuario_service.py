from sqlalchemy.orm import Session
from models.usuario_model import Usuario

def crear_usuario(db: Session, nombre: str, correo: str, rol: str):
    # Verificar si el correo ya existe
    usuario_existente = db.query(Usuario).filter(Usuario.correo == correo).first()
    if usuario_existente:
        raise ValueError("El correo ya está registrado.")

    # Crear un nuevo usuario
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, rol=rol)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario
