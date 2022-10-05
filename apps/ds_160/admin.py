from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.ds_160.models import DS160


@admin.register(DS160)
class DS_160_UploadAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'submitted', 'modified_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
