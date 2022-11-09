from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from .models import MockVisaInterviewSession


@receiver(post_save, sender=MockVisaInterviewSession)
def save_full_recording(sender, instance, created, **kwargs):
    if not created and instance.final is True:
        async_task(
            'apps.mock_visa_interview.tasks.save_full_recording', instance)
