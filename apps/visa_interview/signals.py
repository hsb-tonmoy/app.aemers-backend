from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.visa_interview.models import VisaInterview


@receiver(post_save, sender=VisaInterview)
def update_application_status(sender, instance, created, **kwargs):
    if instance.submitted == True:
        instance.user.application.visa_interview = 2
        instance.user.save()
    else:
        instance.user.application.visa_interview = 0
        instance.user.save()
