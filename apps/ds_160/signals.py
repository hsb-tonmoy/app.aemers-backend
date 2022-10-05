from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.ds_160.models import DS160


@receiver(post_save, sender=DS160)
def update_application_status(sender, instance, created, **kwargs):
    if instance.submitted == True:
        instance.user.application.ds_160_filed = 2
        instance.user.save()
    else:
        instance.user.application.ds_160_filed = 0
        instance.user.save()
