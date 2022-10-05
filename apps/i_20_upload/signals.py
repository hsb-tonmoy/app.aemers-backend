from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.i_20_upload.models import I_20_Upload
from apps.ds_160.models import DS160
from apps.sevis_payment.models import SEVIS_PAYMENT
from apps.visa_fee_payment.models import VisaFeePayment

from django.contrib.auth import get_user_model

User = get_user_model()


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