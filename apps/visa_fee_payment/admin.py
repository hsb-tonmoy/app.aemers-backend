from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.visa_fee_payment.models import VisaFeePayment


@admin.register(VisaFeePayment)
class VisaFeePaymentAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'submitted', 'modified_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
