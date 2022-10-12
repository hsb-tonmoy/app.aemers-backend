from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


class PreDepartureSession(models.Model):
    class Meta:
        verbose_name = _("Pre-Departure Session")
        verbose_name_plural = _("Pre-Departure Sessions")

    history = HistoricalRecords()

    title = models.CharField(_("Title"), max_length=255)
    image = ProcessedImageField(upload_to='pre_departure_sessions/',
                                processors=[ResizeToFill(300, 300)],
                                format='PNG',
                                options={'quality': 60}, default='profiles/avatar.png', null=True, blank=True)
    date = models.DateField(_("Date"), default=timezone.now)
    time = models.TimeField(_("Time"), default=timezone.now)
    location = models.CharField(_("Location"), max_length=255)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   related_name='pre_departure_sessions_created_by', null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.title


class Participant(models.Model):
    class Meta:
        verbose_name = _("Participant")
        verbose_name_plural = _("Participants")

    history = HistoricalRecords()

    pre_departure_session = models.ForeignKey(PreDepartureSession, on_delete=models.CASCADE,
                                              related_name='participants')

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='pre_departure_session')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
