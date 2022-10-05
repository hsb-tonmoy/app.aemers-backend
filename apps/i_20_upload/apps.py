from django.apps import AppConfig


class I20UploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.i_20_upload'

    def ready(self):
        from . import signals
