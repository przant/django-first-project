"""Health check URL configuration."""

from django.urls import path

from . import views

app_name = "healthcheck"

urlpatterns = [
    path("health/live/", views.liveness, name="liveness"),
    path("health/ready/", views.readiness, name="readiness"),
]
