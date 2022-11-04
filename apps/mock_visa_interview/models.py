from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from django.contrib.auth import get_user_model
User = get_user_model()

IMPORTANCE_RATINGS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


def upload_to_path_question(instance, filename):
    path = f'mock_visa_interview/questions/{instance.id}/{filename}'
    return path


class MockVisaInterviewQuestion(models.Model):
    question = models.TextField(verbose_name=_('Question'))
    question_audio = models.FileField(
        _("Question Audio"), upload_to=upload_to_path_question, null=True, blank=True)
    importance = models.PositiveSmallIntegerField(
        _("Importance"), choices=IMPORTANCE_RATINGS, default=1)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='mock_visa_interview_questions_created', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Mock Visa Interview Question')
        verbose_name_plural = _('Mock Visa Interview Questions')

    def __str__(self):
        return self.question


class MockVisaInterviewSession(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mock_visa_interview_sessions')
    created_at = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Mock Visa Interview Session')
        verbose_name_plural = _('Mock Visa Interview Sessions')

    def __str__(self):
        return f"{self.user.first_name} - {self.created_at}"


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    extension = filename.split(".")[-1]
    path = f'mock_visa_interview/{instance.user.username}_{instance.user.id}/{file_name}.{extension}'
    return path


class MockVisaInterviewAnswer(models.Model):
    session = models.ForeignKey(
        MockVisaInterviewSession, on_delete=models.CASCADE, related_name='mock_visa_interview_answers')
    question = models.ForeignKey(
        MockVisaInterviewQuestion, on_delete=models.CASCADE, related_name='answers')
    answer = models.FileField(_("Answer"), upload_to=upload_to_path)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mock_visa_interview_answers')
    created_at = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _('Mock Visa Interview Answer')
        verbose_name_plural = _('Mock Visa Interview Answers')

    def __str__(self):
        return f"{self.user.first_name} - {self.question}"
