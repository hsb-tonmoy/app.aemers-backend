from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.mock_visa_interview.models import MockVisaInterviewAnswer, MockVisaInterviewQuestion, MockVisaInterviewSession
from apps.mock_visa_interview.serializers import MockVisaInterviewAnswerSerializer, MockVisaInterviewQuestionSerializer, MockVisaInterviewSessionSerializer


class MockVisaInterviewAnswerViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewAnswer.objects.all()
    serializer_class = MockVisaInterviewAnswerSerializer


class MockVisaInterviewQuestionViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewQuestion.objects.all()
    serializer_class = MockVisaInterviewQuestionSerializer


class MockVisaInterviewSessionViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewSession.objects.all()
    serializer_class = MockVisaInterviewSessionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
