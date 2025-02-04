from fastapi.testclient import TestClient
from main import app
from models.usuario_model import Usuario, SessionLocal

client = TestClient(app)

def test_crear_usuario():
    # Datos de prueba
    usuario = {
        "nombre": "Juan Perez",
        "correo": "juan@example.com",
        "rol": "admin"
    }

    # Crear usuario
    response = client.post("/api/usuarios/crear", json=usuario)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario creado exitosamente"

    # Verificar que el usuario se guardó en la base de datos
    db = SessionLocal()
    usuario_db = db.query(Usuario).filter(Usuario.correo == usuario["correo"]).first()
    db.close()
    assert usuario_db is not None
    assert usuario_db.nombre == usuario["nombre"]