from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.mock_visa_interview.models import MockVisaInterviewQuestion, MockVisaInterviewSession, MockVisaInterviewAnswer


@admin.register(MockVisaInterviewQuestion)
class MockVisaInterviewQuestionAdmin(SimpleHistoryAdmin):

    list_display = ('question', 'importance', 'created_at', 'created_by')
    ordering = ('id',)


@admin.register(MockVisaInterviewSession)
class MockVisaInterviewSessionAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'created_at',)
    ordering = ('-created_at',)


@admin.register(MockVisaInterviewAnswer)
class MockVisaInterviewAnswerAdmin(SimpleHistoryAdmin):

    list_display = ('user', 'session', 'question', 'created_at')
    ordering = ('id',)
