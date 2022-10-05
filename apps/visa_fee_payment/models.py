from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model

User = get_user_model()


class VisaFeePayment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="visa_fee_payment")
    submitted = models.BooleanField(_("Has submitted?"), default=False)
    modified_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
