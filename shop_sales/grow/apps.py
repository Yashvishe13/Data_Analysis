from django.apps import AppConfig


class GrowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grow'

    def ready(self):
        from . import signals
