from django.apps import AppConfig


class VisaInterviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.visa_interview'

    def ready(self):
        from . import signals
