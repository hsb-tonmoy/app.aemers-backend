from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from django.contrib.auth import get_user_model

User = get_user_model()

PRIORITY_CHOICES = (
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
    (4, 'Urgent'),
)


class NoteCategory(models.Model):
    class Meta:
        verbose_name = _("Note Category")
        verbose_name_plural = _("Note Categories")
        ordering = ["id"]

    name = models.CharField(_('Name'), max_length=150)
    slug = models.SlugField(_('Slug'), max_length=150, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):

    class Meta:

        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        ordering = ["id"]

    history = HistoricalRecords()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='my_notes', null=True, blank=True)

    category = models.ForeignKey(
        NoteCategory, on_delete=models.CASCADE, related_name='notes')

    internal = models.BooleanField(_("Internal Note?"), default=False)
    complete = models.BooleanField(_("Complete?"), default=False)

    priority = models.PositiveSmallIntegerField(
        _("Note Priority"), choices=PRIORITY_CHOICES, default=1)

    def __str__(self):
        return self.title
