from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model

User = get_user_model()


class FileOpening(models.Model):

    class Meta:
        verbose_name = _("Payment Info")
        verbose_name_plural = _("Payment Info")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_opening_payment_info")
    payment_method = models.CharField(
        _("Payment Method"), max_length=255, null=True, blank=True)
    payment_id = models.CharField(
        _("Payment ID"), max_length=255, null=True, blank=True)
    payment_amount = models.CharField(
        _("Payment Amount"), max_length=255, null=True, blank=True)
    payment_currency = models.CharField(
        _("Payment Currency"), max_length=255, null=True, blank=True)

    submitted = models.BooleanField(_("Submitted"), default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class FileOpeningPaymentAmount(models.Model):
    class Meta:
        verbose_name = _("Payment Amount")
        verbose_name_plural = _("Payment Payment")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_opening_payment_amount")

    payment_amount = models.CharField(_("Payment Amount"), max_length=255)

    checked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_opening_checked_by")
    
    modified_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
