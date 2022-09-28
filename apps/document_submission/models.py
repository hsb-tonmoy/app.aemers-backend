from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class DocumentCategory(models.Model):
    class Meta:
        verbose_name = _("Document Category")
        verbose_name_plural = _("Document Categories")
        ordering = ["code"]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=255, default="00")
    slug = models.SlugField(_('Slug'), max_length=150, unique=True)

    def __str__(self):
        return self.name


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    extension = filename.split(".")[-1]
    path = f'documents/{instance.user.username}_{instance.user.id}/{file_name}.{extension}'
    return path


DOCUMENT_STATUS = (
    (0, "Pending"),
    (1, "Accepted"),
    (2, "Rejected"),
)


class Document(models.Model):

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documents')

    category = models.ForeignKey(
        DocumentCategory, on_delete=models.CASCADE, related_name='documents')

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to=upload_to_path)
    checked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_documents')

    status = models.PositiveSmallIntegerField(
        _("Status"), choices=DOCUMENT_STATUS, default=0)

    def __str__(self):
        return self.title
