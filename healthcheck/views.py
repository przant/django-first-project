"""Health check views for monitoring system health."""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["GET"])
def liveness(request: Request) -> Response:
    """Liveness probe to check if the application is running.

    Returns: Response 200 OK status indicating the service is alive
    """
    return Response({"status": "alive"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def readiness(request: Request) -> Response:
    """Readiness probe to check if the application is ready to handle traffic.

    This checks critical services like database connectivity.

    Returns: Response 200 OK if ready, 503 Service Unavailable if not ready
    """
    try:
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return Response({"status": "ready"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": "unavailable", "reason": str(e)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
