from django.apps import AppConfig


class FileOpeningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.file_opening'

    def ready(self):
        from . import signals
