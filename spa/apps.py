"""This module configures the spa application for Django."""

from django.apps import AppConfig


class SpaConfig(AppConfig):
    """Configuration class for the Spa application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spa'

    def ready(self):
        """Import signals for the Spa application."""
        import spa.signals
