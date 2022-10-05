from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.sevis_payment.models import SEVIS_PAYMENT


@admin.register(SEVIS_PAYMENT)
class SEVIS_PAYMENT_UploadAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'submitted', 'modified_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
