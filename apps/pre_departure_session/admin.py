from django.contrib import admin
from apps.pre_departure_session.models import PreDepartureSession, Participant
from simple_history.admin import SimpleHistoryAdmin


@admin.register(PreDepartureSession)
class PreDepartureSessionAdmin(SimpleHistoryAdmin):

    list_display = ('title', 'date', 'time', 'location')
    ordering = ('id',)


@admin.register(Participant)
class ParticipantAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'pre_departure_session', 'created_at',)
    ordering = ('id',)
