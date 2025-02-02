from django.apps import AppConfig


class HealthcheckConfig(AppConfig):
    """Health check application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "healthcheck"
