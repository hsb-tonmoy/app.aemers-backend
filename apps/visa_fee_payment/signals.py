from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.visa_fee_payment.models import VisaFeePayment


@receiver(post_save, sender=VisaFeePayment)
def update_application_status(sender, instance, created, **kwargs):
    if instance.submitted == True:
        instance.user.application.visa_fee_payment = 2
        instance.user.save()
    else:
        instance.user.application.visa_fee_payment = 0
        instance.user.save()
