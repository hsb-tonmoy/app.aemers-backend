from rest_framework import serializers
from apps.visa_interview.models import VisaInterview


class VisaInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisaInterview
        fields = "__all__"
