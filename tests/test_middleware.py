import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_middleware_logging(caplog):
    """
    Verifica que el middleware registra las solicitudes y respuestas correctamente.
    """
    with caplog.at_level("INFO", logger="middleware_logger"):
        response = client.get("/")  # Simula una solicitud GET a la raíz
        assert response.status_code == 404  # Porque no existe una ruta definida aquí

        # Verifica los mensajes reales registrados por el middleware
        assert "Solicitud: GET http://testserver/" in caplog.text
        assert "Respuesta: 404" in caplog.text

