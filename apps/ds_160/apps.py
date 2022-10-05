from django.apps import AppConfig


class Ds160FiledConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ds_160'

    def ready(self):
        from . import signals
