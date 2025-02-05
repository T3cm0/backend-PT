from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

# Configuración del logger
logger = logging.getLogger("middleware_logger")
logging.basicConfig(level=logging.INFO)


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware para registrar información de solicitudes y respuestas.
    """

    async def dispatch(self, request: Request, call_next):
        # Registrar detalles de la solicitud
        logger.info(f"Solicitud: {request.method} {request.url}")

        # Procesar la solicitud y obtener la respuesta
        response: Response = await call_next(request)

        # Registrar detalles de la respuesta
        logger.info(f"Respuesta: {response.status_code}")

        return response
