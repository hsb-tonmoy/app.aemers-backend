from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from apps.file_opening.models import FileOpening

from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=FileOpening)
def update_application_status(sender, instance, created, **kwargs):
    if created:
        instance.user.application.file_opening = 2
        instance.user.save()
        notify.send(instance, recipient=instance.user, verb='opened file', action_object=instance,
                    level='success',  description=f'You have successfully opened the file!')
