from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.sevis_payment.models import SEVIS_PAYMENT


@receiver(post_save, sender=SEVIS_PAYMENT)
def update_application_status(sender, instance, created, **kwargs):
    if instance.submitted == True:
        instance.user.application.sevis_payment = 2
        instance.user.save()
    else:
        instance.user.application.sevis_payment = 0
        instance.user.save()
