from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from .models import Document

from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Document)
def document_upload_notify(sender, instance, created, **kwargs):
    if created:
        try:
            managers_queryset = instance.user.managers.all()
        except User.RelatedObjectDoesNotExist:
            return
        for manager in managers_queryset:
            notify.send(sender=instance.user, recipient=manager.manager, verb="uploaded",
                        action_object=instance, level="success", timestamp=instance.uploaded_at)
