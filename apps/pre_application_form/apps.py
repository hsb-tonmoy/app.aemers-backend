from django.apps import AppConfig


class PreApplicationFormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pre_application_form'

    def ready(self):
        from . import signals
