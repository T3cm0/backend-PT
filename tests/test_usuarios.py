import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_usuario_nuevo():
    response = client.post(
        "/api/usuarios/crear",
        json={
            "nombre": "Nuevo Usuario",
            "correo": "nuevo.usuario@example.com",
            "rol": "Administrador"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Usuario creado exitosamente"
    assert data["usuario"]["nombre"] == "Nuevo Usuario"
    assert data["usuario"]["correo"] == "nuevo.usuario@example.com"
    assert data["usuario"]["rol"] == "Administrador"


def test_crear_usuario_correo_duplicado():
    client.post(
        "/api/usuarios/crear",
        json={
            "nombre": "Prueba Usuario",
            "correo": "duplicado@example.com",
            "rol": "Estudiante"
        }
    )
    response = client.post(
        "/api/usuarios/crear",
        json={
            "nombre": "Otro Usuario",
            "correo": "duplicado@example.com",
            "rol": "Estudiante"
        }
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "El correo ya está registrado."

def test_crear_usuario_correo_invalido():
    response = client.post(
        "/api/usuarios/crear",
        json={
            "nombre": "Usuario Inválido",
            "correo": "correo-invalido",
            "rol": "Estudiante"
        }
    )
    assert response.status_code == 422
    data = response.json()
    assert "value is not a valid email address" in data["detail"][0]["msg"]

def test_crear_usuario_campos_faltantes():
    response = client.post(
        "/api/usuarios/crear",
        json={
            "nombre": "Sin Correo",
            "rol": "Estudiante"
        }
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["loc"] == ["body", "correo"]
