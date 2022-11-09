from django.apps import AppConfig


class MockVisaInterviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mock_visa_interview'

    def ready(self):
        from . import signals
