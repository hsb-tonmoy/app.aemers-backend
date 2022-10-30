from rest_framework import serializers
from apps.mock_visa_interview.models import MockVisaInterviewQuestion, MockVisaInterviewSession, MockVisaInterviewAnswer


class MockVisaInterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewQuestion
        fields = "__all__"


class MockVisaInterviewSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewSession
        fields = "__all__"


class MockVisaInterviewAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewAnswer
        fields = "__all__"
