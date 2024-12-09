"""App configuration."""

from django.apps import AppConfig


class DjangoPipecatConfig(AppConfig):
    """App configuration for django-pipecat."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_pipecat"
