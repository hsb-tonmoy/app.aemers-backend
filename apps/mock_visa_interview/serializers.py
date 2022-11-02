from rest_framework import serializers
from apps.mock_visa_interview.models import MockVisaInterviewQuestion, MockVisaInterviewSession, MockVisaInterviewAnswer


class MockVisaInterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewQuestion
        fields = "__all__"


class MockVisaInterviewAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewAnswer
        fields = "__all__"


class MockVisaInterviewAnswerRetrieveSerializer(serializers.ModelSerializer):
    question = MockVisaInterviewQuestionSerializer(read_only=True)

    class Meta:
        model = MockVisaInterviewAnswer
        fields = "__all__"


class MockVisaInterviewSessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockVisaInterviewSession
        fields = "__all__"


class MockVisaInterviewSessionRetrieveSerializer(serializers.ModelSerializer):
    mock_visa_interview_answers = MockVisaInterviewAnswerRetrieveSerializer(
        many=True, read_only=True)

    class Meta:
        model = MockVisaInterviewSession
        fields = "__all__"
