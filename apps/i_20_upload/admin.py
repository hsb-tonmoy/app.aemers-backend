from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.i_20_upload.models import I_20_Upload


@admin.register(I_20_Upload)
class I_20_UploadAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'status', 'checked_by', 'uploaded_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
