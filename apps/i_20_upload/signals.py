from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from apps.i_20_upload.models import I_20_Upload
from apps.ds_160.models import DS160
from apps.sevis_payment.models import SEVIS_PAYMENT
from apps.visa_fee_payment.models import VisaFeePayment
from apps.visa_interview.models import VisaInterview
from notifications.signals import notify

from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=I_20_Upload)
def update_application_status(sender, instance, created, **kwargs):
    if instance.status == 1:
        instance.user.application.i_20_upload = 2
        instance.user.save()
        notify.send(instance, recipient=instance.user, verb='approved I-20', action_object=instance,
                    level='success',  description=f'Your I-20 has been accepted!')
    else:
        instance.user.application.i_20_upload = 0
        instance.user.save()
        if not created:
            notify.send(instance, recipient=instance.user, verb='rejected I-20', action_object=instance,
                        level='error',  description=f'Your I-20 has been rejected!')


@receiver(pre_delete, sender=I_20_Upload)
def update_application_status_if_deleted(sender, instance, using, **kwargs):
    instance.user.application.i_20_upload = 0
    instance.user.save()


@receiver(post_save, sender=I_20_Upload)
def create_ds_160_if_not_exists(sender, instance, created, **kwargs):
    try:
        DS160.objects.get(user=instance.user)
    except DS160.DoesNotExist:
        DS160.objects.create(user=instance.user)


@receiver(post_save, sender=I_20_Upload)
def create_sevis_payment_if_not_exists(sender, instance, created, **kwargs):
    try:
        SEVIS_PAYMENT.objects.get(user=instance.user)
    except SEVIS_PAYMENT.DoesNotExist:
        SEVIS_PAYMENT.objects.create(user=instance.user)


@receiver(post_save, sender=I_20_Upload)
def create_visa_fee_payment_if_not_exists(sender, instance, created, **kwargs):
    try:
        VisaFeePayment.objects.get(user=instance.user)
    except VisaFeePayment.DoesNotExist:
        VisaFeePayment.objects.create(user=instance.user)


@receiver(post_save, sender=I_20_Upload)
def create_visa_interview_if_not_exists(sender, instance, created, **kwargs):
    try:
        VisaInterview.objects.get(user=instance.user)
    except VisaInterview.DoesNotExist:
        VisaInterview.objects.create(user=instance.user)
