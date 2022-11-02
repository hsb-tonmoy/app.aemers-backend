from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.mock_visa_interview.models import MockVisaInterviewAnswer, MockVisaInterviewQuestion, MockVisaInterviewSession
from apps.mock_visa_interview.serializers import MockVisaInterviewAnswerSerializer, MockVisaInterviewQuestionSerializer, MockVisaInterviewSessionListSerializer, MockVisaInterviewSessionRetrieveSerializer


class MockVisaInterviewAnswerViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewAnswer.objects.all()
    serializer_class = MockVisaInterviewAnswerSerializer


class MockVisaInterviewQuestionViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewQuestion.objects.all()
    serializer_class = MockVisaInterviewQuestionSerializer


class MockVisaInterviewSessionViewset(viewsets.ModelViewSet):
    queryset = MockVisaInterviewSession.objects.all()
    serializer_class = MockVisaInterviewSessionListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    retrieve_serializer_class = MockVisaInterviewSessionRetrieveSerializer

    def get_serializer_class(self):

        if self.action == 'retrieve':
            if hasattr(self, 'retrieve_serializer_class'):
                return self.retrieve_serializer_class

        return super(MockVisaInterviewSessionViewset, self).get_serializer_class()
