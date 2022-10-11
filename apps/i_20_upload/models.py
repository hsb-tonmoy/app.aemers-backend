from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model

User = get_user_model()


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    extension = filename.split(".")[-1]
    path = f'i_20/{instance.user.username}_{instance.user.id}/{file_name}.{extension}'
    return path


DOCUMENT_STATUS = (
    (0, "Pending"),
    (1, "Accepted"),
    (2, "Rejected"),
)


class I_20_Upload(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="i_20")
    title = models.CharField(
        _('Title'),  max_length=255, blank=True, null=True)
    document = models.FileField(upload_to=upload_to_path)
    uploaded_at = models.DateTimeField(_('Uploaded At'), auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        _("Status"), choices=DOCUMENT_STATUS, default=0)
    checked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_i_20')

    history = HistoricalRecords()
