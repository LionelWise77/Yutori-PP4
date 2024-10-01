from django.apps import AppConfig


class SpaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spa'

    def ready(self):
        import spa.signals