from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.visa_interview.models import VisaInterview


@admin.register(VisaInterview)
class VisaInterviewAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'submitted', 'modified_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('id',)
