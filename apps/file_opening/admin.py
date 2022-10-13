from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.file_opening.models import FileOpening, FileOpeningPaymentAmount


@admin.register(FileOpening)
class FileOpeningAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'submitted', 'created_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)


@admin.register(FileOpeningPaymentAmount)
class FileOpeningPaymentAmountAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'payment_amount', 'checked_by', 'modified_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
